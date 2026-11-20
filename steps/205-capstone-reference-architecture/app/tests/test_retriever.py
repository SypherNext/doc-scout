"""Tests for research_assistant.rag.retriever.Retriever."""

from __future__ import annotations

from research_assistant.ingestion.pipeline import IngestionPipeline
from research_assistant.rag.retriever import Retriever


def test_query_against_empty_collection_returns_no_chunks(retriever: Retriever) -> None:
    assert retriever.query("anything") == []


def test_query_returns_ingested_chunk(
    ingestion_pipeline: IngestionPipeline, retriever: Retriever
) -> None:
    ingestion_pipeline.ingest_document(
        "Python was created by Guido van Rossum and released in 1991.",
        doc_id="python_intro",
    )

    results = retriever.query("Who created Python?", top_k=3)

    assert len(results) >= 1
    assert results[0].doc_id == "python_intro"
    assert "Guido" in results[0].document


def test_query_respects_top_k(
    ingestion_pipeline: IngestionPipeline, retriever: Retriever
) -> None:
    for i in range(5):
        ingestion_pipeline.ingest_document(
            f"Document number {i} about topic {i}.", doc_id=f"doc{i}"
        )

    results = retriever.query("topic", top_k=2)
    assert len(results) <= 2


def test_query_scores_are_bounded_between_zero_and_one(
    ingestion_pipeline: IngestionPipeline, retriever: Retriever
) -> None:
    ingestion_pipeline.ingest_document("Some content about machine learning.", doc_id="ml_doc")

    results = retriever.query("machine learning")
    for result in results:
        assert 0.0 <= result.score <= 1.0
