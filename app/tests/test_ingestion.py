"""Tests for research_assistant.ingestion.pipeline.IngestionPipeline.

Embeddings are mocked (see conftest.fake_openai_client); Chroma itself is
real, backed by a temp directory, per the Reference Architecture's guidance
on mocking depth.
"""

from __future__ import annotations

from research_assistant.ingestion.pipeline import IngestionPipeline


def test_ingest_document_returns_chunk_count(ingestion_pipeline: IngestionPipeline) -> None:
    text = "Python is a language. " * 20
    chunk_count = ingestion_pipeline.ingest_document(text, doc_id="doc1")
    assert chunk_count > 0


def test_ingest_empty_document_returns_zero_without_calling_embeddings(
    ingestion_pipeline: IngestionPipeline,
) -> None:
    chunk_count = ingestion_pipeline.ingest_document("", doc_id="empty_doc")
    assert chunk_count == 0
    ingestion_pipeline._embed_client.embed.assert_not_called()


def test_ingested_chunks_are_retrievable_from_chroma(
    ingestion_pipeline: IngestionPipeline,
) -> None:
    ingestion_pipeline.ingest_document("Python was created by Guido van Rossum.", doc_id="doc1")

    stored = ingestion_pipeline._collection.get(ids=["doc1_chunk_0"])
    assert stored["ids"] == ["doc1_chunk_0"]
    assert "Guido" in stored["documents"][0]
    assert stored["metadatas"][0]["doc_id"] == "doc1"


def test_ingest_stores_source_and_custom_metadata(
    ingestion_pipeline: IngestionPipeline,
) -> None:
    ingestion_pipeline.ingest_document(
        "Some content.", doc_id="doc2", source="wikipedia", metadata={"lang": "en"}
    )
    stored = ingestion_pipeline._collection.get(ids=["doc2_chunk_0"])
    assert stored["metadatas"][0]["source"] == "wikipedia"
    assert stored["metadatas"][0]["lang"] == "en"


def test_reingesting_same_doc_id_overwrites_previous_chunks(
    ingestion_pipeline: IngestionPipeline,
) -> None:
    ingestion_pipeline.ingest_document("First version of the document.", doc_id="doc3")
    ingestion_pipeline.ingest_document("Second version of the document.", doc_id="doc3")

    stored = ingestion_pipeline._collection.get(ids=["doc3_chunk_0"])
    assert "Second version" in stored["documents"][0]
