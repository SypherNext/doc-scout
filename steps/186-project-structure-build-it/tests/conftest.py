"""Shared pytest fixtures.

External APIs (Anthropic, OpenAI) are always mocked at the boundary: the
``OpenAIClient.embed`` / ``AnthropicClient.generate_structured`` methods,
not the HTTP layer underneath them, and never the Chroma query itself --
per the Capstone Reference Architecture's "mocking depth" pitfall, real
Chroma distance computation runs in every test that touches retrieval.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from research_assistant.cache import QueryCache
from research_assistant.ingestion.pipeline import IngestionPipeline
from research_assistant.rag.generator import Generator
from research_assistant.rag.retriever import Retriever


@pytest.fixture
def fake_openai_client() -> MagicMock:
    """A mock OpenAIClient whose embed() returns small, deterministic vectors.

    Vectors are built from a hash of the input text so that similar calls
    (and repeated ingestion of the same text) are stable across a test run,
    while unrelated texts land at different points in the vector space --
    good enough for exercising Chroma's real cosine search without a live
    embedding API call.
    """
    client = MagicMock()

    def _embed(text: str) -> list[float]:
        seed = sum(ord(c) for c in text) % 997
        return [((seed + i) % 101) / 100.0 for i in range(8)]

    client.embed.side_effect = _embed
    return client


@pytest.fixture
def fake_anthropic_client() -> MagicMock:
    """A mock AnthropicClient whose generate_structured() echoes a canned answer."""
    client = MagicMock()
    client.generate_structured.return_value = {
        "answer": "Python was created by Guido van Rossum.",
        "citations": [{"source_doc_id": "python_intro", "relevance_score": 0.91}],
    }
    return client


@pytest.fixture
def chroma_path(tmp_path) -> str:
    return str(tmp_path / "rag_db")


@pytest.fixture
def ingestion_pipeline(fake_openai_client: MagicMock, chroma_path: str) -> IngestionPipeline:
    return IngestionPipeline(
        embed_client=fake_openai_client,
        chroma_path=chroma_path,
        collection_name="test_docs",
        chunk_size=50,
        chunk_overlap=10,
    )


@pytest.fixture
def retriever(fake_openai_client: MagicMock, chroma_path: str) -> Retriever:
    # Shares chroma_path with ingestion_pipeline's collection name so a test
    # can ingest then retrieve against the same on-disk store.
    return Retriever(
        embed_client=fake_openai_client,
        chroma_path=chroma_path,
        collection_name="test_docs",
    )


@pytest.fixture
def generator(fake_anthropic_client: MagicMock) -> Generator:
    return Generator(llm_client=fake_anthropic_client)


@pytest.fixture
def query_cache(tmp_path) -> QueryCache:
    cache = QueryCache(cache_dir=str(tmp_path / "cache"), ttl_seconds=3600)
    yield cache
    cache.close()
