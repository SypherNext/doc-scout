"""Chunk, embed, and store documents in Chroma.

Follows the Embeddings lesson's ``PersistentVectorSearch`` pattern (a
``chromadb.PersistentClient`` collection created with cosine HNSW), extended
with the RAG lesson's chunking-with-metadata.

NOTE ON BATCHING: the RAG lesson's own teaching code embeds chunks in
batches of 100 via a direct ``openai.embeddings.create(input=<list>)``
call. Course 2's shared ``OpenAIClient.embed()`` (the client this pipeline
actually uses, per the "don't reinvent a client" rule) only embeds one
string at a time -- there is no batch method on it. This pipeline therefore
calls ``embed()`` once per chunk rather than once per 100 chunks: correct,
but more API round-trips than the lesson's own batching example. Flagged
for the integration pass: either Course 2 adds a batch-embed method, or
this stays a known, documented trade-off of reusing the shared client.
"""

from __future__ import annotations

import logging
from typing import Any, cast

import chromadb

from research_assistant.exceptions import IngestionError
from research_assistant.ingestion.chunker import chunk_text
from research_assistant.llm.clients import OpenAIClient

logger = logging.getLogger(__name__)


class IngestionPipeline:
    """Ingest documents into the Chroma vector store for RAG."""

    def __init__(
        self,
        embed_client: OpenAIClient,
        chroma_path: str,
        collection_name: str = "rag_docs",
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ) -> None:
        """
        Args:
            embed_client: Client used to embed chunks before storage. Its
                embedding model is fixed at construction
                (``OpenAIClient(embedding_model=...)``), not passed per call.
            chroma_path: Filesystem path for the persistent Chroma store.
                Should be an absolute path (or resolved relative to a fixed
                project root) so the collection resolves to the same place
                whether the process is started from the project root, from
                a test runner's working directory, or inside Docker.
            collection_name: Name of the Chroma collection to use.
            chunk_size: Target tokens per chunk, passed to ``chunk_text``.
            chunk_overlap: Overlap tokens between adjacent chunks.
        """
        self._embed_client = embed_client
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap
        try:
            self._chroma = chromadb.PersistentClient(path=chroma_path)
            self._collection = self._chroma.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
            )
        except Exception as exc:  # pragma: no cover - chromadb's own errors vary by backend
            raise IngestionError(f"Could not open Chroma collection at {chroma_path!r}") from exc

    def ingest_document(
        self,
        text: str,
        doc_id: str,
        source: str | None = None,
        metadata: dict[str, str] | None = None,
    ) -> int:
        """Chunk, embed, and store a single document.

        Args:
            text: Full document text. An empty document is handled
                gracefully: it returns 0 without touching Chroma or the
                embedding API.
            doc_id: Unique identifier for the document. Re-ingesting the
                same ``doc_id`` overwrites its previous chunks (stored via
                Chroma's ``upsert``, not ``add``, specifically so this holds).
            source: Optional human-readable source label (URL, filename).
            metadata: Optional extra metadata stored alongside every chunk.

        Returns:
            Number of chunks stored.
        """
        chunks = chunk_text(text, chunk_size=self._chunk_size, chunk_overlap=self._chunk_overlap)
        if not chunks:
            logger.info("Ingest %s: document is empty, stored 0 chunks", doc_id)
            return 0

        chunk_ids = [f"{doc_id}_chunk_{i}" for i in range(len(chunks))]
        base_metadata = {"doc_id": doc_id}
        if source:
            base_metadata["source"] = source
        if metadata:
            base_metadata.update(metadata)
        metadatas = [{**base_metadata, "chunk_index": i} for i in range(len(chunks))]

        # One embed() call per chunk: see the module docstring's note on
        # why this isn't batched the way the RAG lesson's own example is.
        embeddings = [self._embed_client.embed(chunk) for chunk in chunks]

        try:
            # upsert, not add: re-ingesting the same doc_id must replace its
            # previous chunks rather than silently keeping the old ones
            # (Chroma's add() does not overwrite existing ids). chromadb's
            # stubs are stricter than its documented runtime API for both
            # of these; see the matching note in rag/retriever.py.
            self._collection.upsert(
                embeddings=cast(Any, embeddings),
                documents=chunks,
                ids=chunk_ids,
                metadatas=cast(Any, metadatas),
            )
        except Exception as exc:  # pragma: no cover - backend-specific
            raise IngestionError(f"Failed to store chunks for {doc_id!r} in Chroma") from exc

        logger.info("Ingest %s: stored %d chunks", doc_id, len(chunks))
        return len(chunks)
