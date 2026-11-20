"""Tests for research_assistant.cache.QueryCache."""

from __future__ import annotations

import time

from research_assistant.cache import QueryCache


def test_make_key_is_deterministic_for_the_same_question() -> None:
    assert QueryCache.make_key("What is Python?") == QueryCache.make_key("What is Python?")


def test_make_key_is_case_and_whitespace_insensitive() -> None:
    assert QueryCache.make_key("What is Python?") == QueryCache.make_key("  WHAT IS PYTHON?  ")


def test_make_key_differs_for_different_doc_scope() -> None:
    key_a = QueryCache.make_key("What is Python?", doc_ids=["doc1"])
    key_b = QueryCache.make_key("What is Python?", doc_ids=["doc2"])
    assert key_a != key_b


def test_cache_miss_returns_none(query_cache: QueryCache) -> None:
    assert query_cache.get("nonexistent-key") is None


def test_cache_hit_returns_stored_value(query_cache: QueryCache) -> None:
    key = QueryCache.make_key("hello")
    query_cache.set(key, {"answer": "world", "citations": [], "latency_ms": 5})

    cached = query_cache.get(key)
    assert cached == {"answer": "world", "citations": [], "latency_ms": 5}


def test_cache_expires_after_ttl(tmp_path) -> None:
    cache = QueryCache(cache_dir=str(tmp_path / "cache"), ttl_seconds=1)
    try:
        key = QueryCache.make_key("short-lived")
        cache.set(key, "value")
        assert cache.get(key) == "value"

        time.sleep(1.2)
        assert cache.get(key) is None
    finally:
        cache.close()


def test_set_accepts_a_ttl_override(query_cache: QueryCache) -> None:
    key = QueryCache.make_key("overridden-ttl")
    query_cache.set(key, "value", ttl_seconds=10)
    assert query_cache.get(key) == "value"


def test_get_json_decodes_a_json_string(query_cache: QueryCache) -> None:
    key = "raw-json-key"
    query_cache._cache.set(key, '{"answer": "hi"}', expire=3600)
    assert query_cache.get_json(key) == {"answer": "hi"}


def test_len_reflects_number_of_entries(query_cache: QueryCache) -> None:
    assert len(query_cache) == 0
    query_cache.set(QueryCache.make_key("one"), "a")
    query_cache.set(QueryCache.make_key("two"), "b")
    assert len(query_cache) == 2
