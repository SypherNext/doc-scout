"""Disk-persistent response cache.

Caches at the API level: the key is a SHA256 hash of the question (plus any
ingested-document scope), and the value is the full serialised
``AnswerResponse`` -- not just the raw LLM text. A cache hit therefore skips
both the embedding call and the Chroma query, not only the LLM call. See the
Capstone Reference Architecture's "Cache at the API level" decision for the
reasoning and the accepted staleness trade-off (bounded by the TTL).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from diskcache import Cache

from research_assistant.exceptions import CacheError


class QueryCache:
    """A ``diskcache``-backed cache keyed by SHA256(question)."""

    def __init__(self, cache_dir: str | Path, ttl_seconds: int = 3600) -> None:
        """Open (creating if needed) a disk cache at ``cache_dir``.

        Args:
            cache_dir: Directory the cache's SQLite-backed store lives in.
                Must survive container restarts (mount it as a volume).
            ttl_seconds: Default seconds an entry stays valid for.
        """
        self._ttl_seconds = ttl_seconds
        try:
            self._cache = Cache(str(cache_dir))
        except OSError as exc:
            raise CacheError(f"Could not open cache directory {cache_dir!r}") from exc

    @staticmethod
    def make_key(question: str, doc_ids: list[str] | None = None) -> str:
        """Build the cache key: SHA256 of the normalised question and doc scope.

        Args:
            question: The raw user question.
            doc_ids: Optional explicit set of document ids the answer is
                scoped to. Included in the hash so the same question asked
                against a different document scope is a different cache
                entry.
        """
        normalised_question = question.strip().lower()
        scope = ",".join(sorted(doc_ids)) if doc_ids else ""
        payload = f"{normalised_question}|{scope}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def get(self, key: str) -> Any | None:
        """Return the cached value for ``key``, or ``None`` on a miss or expiry."""
        try:
            return self._cache.get(key, default=None)
        except OSError as exc:
            raise CacheError("Failed to read from the query cache") from exc

    def set(self, key: str, value: Any, ttl_seconds: int | None = None) -> None:
        """Store ``value`` under ``key`` for ``ttl_seconds`` (default: the cache's own TTL)."""
        try:
            self._cache.set(key, value, expire=ttl_seconds or self._ttl_seconds)
        except OSError as exc:
            raise CacheError("Failed to write to the query cache") from exc

    def get_json(self, key: str) -> dict[str, Any] | None:
        """Like :meth:`get`, but the value is JSON-decoded if it was stored as a string."""
        value = self.get(key)
        if isinstance(value, str):
            return json.loads(value)
        return value

    def close(self) -> None:
        """Flush and close the underlying disk cache. Safe to call more than once."""
        self._cache.close()

    def __len__(self) -> int:
        return len(self._cache)
