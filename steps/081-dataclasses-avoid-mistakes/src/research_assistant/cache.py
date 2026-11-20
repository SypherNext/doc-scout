"""Query caching for repeat questions.

QueryCache wraps diskcache.Cache and keys entries by a hash of the
query text plus the document ids it was asked against, so the same
question against a different document set is a different cache entry.

CacheContext is a context manager (class-based __enter__/__exit__,
the style from the Context Managers lesson) that opens and closes the
underlying diskcache.Cache resource safely, even if the block raises.
"""
import hashlib
from pathlib import Path

import diskcache

from .exceptions import CacheError


class QueryCache:
    """Caches query results, keyed by sha256(query + sorted doc_ids)."""

    def __init__(self, cache_dir: str = "./cache", ttl_seconds: int = 3600):
        self._cache = diskcache.Cache(cache_dir)
        self.ttl_seconds = ttl_seconds

    @staticmethod
    def make_key(query: str, doc_ids: list[str]) -> str:
        raw = query + "|" + ",".join(sorted(doc_ids))
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def get(self, query: str, doc_ids: list[str]):
        try:
            return self._cache.get(self.make_key(query, doc_ids))
        except Exception as exc:
            raise CacheError(f"Could not read from cache: {exc}") from exc

    def set(self, query: str, doc_ids: list[str], value) -> None:
        try:
            self._cache.set(self.make_key(query, doc_ids), value, expire=self.ttl_seconds)
        except Exception as exc:
            raise CacheError(f"Could not write to cache: {exc}") from exc

    def close(self) -> None:
        self._cache.close()


class CacheContext:
    """Context manager that opens a QueryCache on __enter__ and
    guarantees it is closed on __exit__, even if the block raises."""

    def __init__(self, cache_dir: str = "./cache", ttl_seconds: int = 3600):
        self.cache_dir = cache_dir
        self.ttl_seconds = ttl_seconds
        self._cache: QueryCache | None = None

    def __enter__(self) -> QueryCache:
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)
        self._cache = QueryCache(self.cache_dir, self.ttl_seconds)
        return self._cache

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._cache is not None:
            self._cache.close()
        # Returning False (or None) propagates any exception from the block.
        return False
