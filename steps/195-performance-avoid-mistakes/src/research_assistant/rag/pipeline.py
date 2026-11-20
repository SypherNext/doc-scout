"""Orchestrates the full RAG request: cache check -> retrieve -> generate -> cache store."""

from __future__ import annotations

import time
from dataclasses import dataclass

from research_assistant.cache import QueryCache
from research_assistant.models import AnswerResponse
from research_assistant.rag.generator import Generator
from research_assistant.rag.retriever import Retriever


@dataclass
class PipelineResult:
    """What ``RAGPipeline.answer`` returns: the response, plus whether it was a cache hit."""

    response: AnswerResponse
    cache_hit: bool


class RAGPipeline:
    """Embed query -> retrieve chunks -> build prompt -> call LLM -> cache the result."""

    def __init__(
        self,
        retriever: Retriever,
        generator: Generator,
        cache: QueryCache,
        top_k: int = 3,
    ) -> None:
        self._retriever = retriever
        self._generator = generator
        self._cache = cache
        self._top_k = top_k

    def answer(self, question: str) -> PipelineResult:
        """Answer ``question``, serving a cached response when available.

        Caching happens at this level (the full response, including
        citations), not inside the generator: a cache hit skips the
        embedding call and the Chroma query as well as the LLM call. See
        the Capstone Reference Architecture's caching decision for the
        staleness trade-off this implies.
        """
        cache_key = QueryCache.make_key(question)
        cached = self._cache.get_json(cache_key)
        if cached is not None:
            return PipelineResult(response=AnswerResponse(**cached), cache_hit=True)

        start = time.perf_counter()
        chunks = self._retriever.query(question, top_k=self._top_k)
        answer = self._generator.generate_answer(question, chunks)
        elapsed_ms = round((time.perf_counter() - start) * 1000)
        answer = answer.model_copy(update={"latency_ms": elapsed_ms})

        self._cache.set(cache_key, answer.model_dump())
        return PipelineResult(response=answer, cache_hit=False)
