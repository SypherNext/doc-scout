"""Embed a query and fetch the top-K most relevant chunks from Chroma."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, cast

import chromadb

from research_assistant.exceptions import IngestionError
from research_assistant.llm.clients import OpenAIClient

logger = logging.getLogger(__name__)


@dataclass
class RetrievedChunk:
    """One chunk returned by a retrieval query."""

    document: str
    doc_id: str
    score: float
    metadata: dict[str, object]


class Retriever:
    """Retrieve relevant chunks for a question via Chroma cosine search."""

    def __init__(
        self,
        embed_client: OpenAIClient,
        chroma_path: str,
        collection_name: str = "rag_docs",
    ) -> None:
        self._embed_client = embed_client
        try:
            self._chroma = chromadb.PersistentClient(path=chroma_path)
            self._collection = self._chroma.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"},
            )
        except Exception as exc:  # pragma: no cover - backend-specific
            raise IngestionError(f"Could not open Chroma collection at {chroma_path!r}") from exc

    def query(self, text: str, top_k: int = 5) -> list[RetrievedChunk]:
        """Return the top-K chunks most relevant to ``text``.

        Args:
            text: Natural-language question.
            top_k: Number of chunks to retrieve.

        Returns:
            Chunks ordered by descending relevance. Empty if the collection
            has no documents, or if the question matches nothing (never
            raises for "no results": the caller decides how to respond).
        """
        if self._collection.count() == 0:
            return []

        query_embedding = self._embed_client.embed(text)

        results = self._collection.query(
            # chromadb's stubs are stricter than its documented runtime API
            # (they only name numpy/array types); a plain list of floats is
            # accepted and is exactly what OpenAIClient.embed returns.
            query_embeddings=cast(Any, [query_embedding]),
            n_results=min(top_k, self._collection.count()),
        )

        documents = results["documents"][0] if results["documents"] else []
        distances = results["distances"][0] if results["distances"] else []
        metadatas = results["metadatas"][0] if results["metadatas"] else []

        chunks: list[RetrievedChunk] = []
        for document, distance, metadata in zip(documents, distances, metadatas):
            # Chroma's cosine space returns a distance in [0, 2]; similarity = 1 - distance.
            score = round(max(0.0, 1.0 - distance), 4)
            chunks.append(
                RetrievedChunk(
                    document=document,
                    doc_id=str(metadata.get("doc_id", "unknown")),
                    score=score,
                    metadata=dict(metadata),
                )
            )
        return chunks
