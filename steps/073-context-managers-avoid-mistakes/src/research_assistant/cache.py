"""Query caching for repeat questions.

This is a first version, written before the project has a real
exception hierarchy. Error Handling later wraps the get/set bodies so
that cache failures raise CacheError instead of leaking diskcache's
own exceptions.
"""
import hashlib
from pathlib import Path

import diskcache


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
        return self._cache.get(self.make_key(query, doc_ids))

    def set(self, query: str, doc_ids: list[str], value) -> None:
        self._cache.set(self.make_key(query, doc_ids), value, expire=self.ttl_seconds)

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
        return False
