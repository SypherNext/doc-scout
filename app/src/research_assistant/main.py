"""FastAPI app: wires config, logging, auth, ingestion, and the RAG pipeline."""

from __future__ import annotations

import hashlib
import logging
import time
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from research_assistant.auth import verify_bearer_token
from research_assistant.cache import QueryCache
from research_assistant.config import load_config
from research_assistant.exceptions import (
    AuthError,
    CacheError,
    IngestionError,
    LLMAPIError,
    LLMTimeoutError,
    MissingTokenError,
    RateLimitError,
    ResearchAssistantError,
)
from research_assistant.ingestion.pipeline import IngestionPipeline
from research_assistant.llm.clients import AnthropicClient, OpenAIClient
from research_assistant.logging_config import configure_logging
from research_assistant.models import (
    AskRequest,
    ErrorResponse,
    IngestRequest,
    IngestResponse,
)
from research_assistant.rag.generator import Generator
from research_assistant.rag.pipeline import RAGPipeline
from research_assistant.rag.retriever import Retriever

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Build every stateful collaborator once per process and tear them down on shutdown."""
    settings = load_config()
    configure_logging(log_dir=settings.log_dir)

    openai_client = OpenAIClient(
        api_key=settings.openai_api_key, embedding_model=settings.embedding_model
    )
    anthropic_client = AnthropicClient(
        api_key=settings.anthropic_api_key, model=settings.anthropic_model
    )
    cache = QueryCache(cache_dir=settings.cache_dir, ttl_seconds=settings.cache_ttl_seconds)

    app.state.settings = settings
    app.state.cache = cache
    app.state.ingestion_pipeline = IngestionPipeline(
        embed_client=openai_client,
        chroma_path=settings.chroma_path,
        collection_name=settings.collection_name,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )
    retriever = Retriever(
        embed_client=openai_client,
        chroma_path=settings.chroma_path,
        collection_name=settings.collection_name,
    )
    generator = Generator(llm_client=anthropic_client)
    app.state.rag_pipeline = RAGPipeline(
        retriever=retriever, generator=generator, cache=cache, top_k=settings.top_k
    )

    try:
        yield
    finally:
        cache.close()


app = FastAPI(title="Doc Scout - AI Research Assistant", lifespan=lifespan)


def _error_body(error: str, detail: str) -> dict[str, str]:
    return ErrorResponse(error=error, detail=detail).model_dump()


@app.exception_handler(AuthError)
async def _handle_auth_error(request: Request, exc: AuthError) -> JSONResponse:
    status_code = 401 if isinstance(exc, MissingTokenError) else 403
    return JSONResponse(status_code=status_code, content=_error_body("auth_error", str(exc)))


@app.exception_handler(LLMTimeoutError)
async def _handle_llm_timeout(request: Request, exc: LLMTimeoutError) -> JSONResponse:
    return JSONResponse(status_code=408, content=_error_body("llm_timeout", str(exc)))


@app.exception_handler(RateLimitError)
async def _handle_rate_limit(request: Request, exc: RateLimitError) -> JSONResponse:
    return JSONResponse(status_code=429, content=_error_body("rate_limited", str(exc)))


@app.exception_handler(LLMAPIError)
async def _handle_llm_api_error(request: Request, exc: LLMAPIError) -> JSONResponse:
    return JSONResponse(status_code=502, content=_error_body("llm_api_error", str(exc)))


@app.exception_handler(IngestionError)
async def _handle_ingestion_error(request: Request, exc: IngestionError) -> JSONResponse:
    return JSONResponse(status_code=422, content=_error_body("ingestion_error", str(exc)))


@app.exception_handler(CacheError)
async def _handle_cache_error(request: Request, exc: CacheError) -> JSONResponse:
    return JSONResponse(status_code=500, content=_error_body("cache_error", str(exc)))


@app.exception_handler(ResearchAssistantError)
async def _handle_generic_error(request: Request, exc: ResearchAssistantError) -> JSONResponse:
    # Catch-all for the package's own error hierarchy. Never leaks a stack
    # trace or internal path: only the exception's own message.
    return JSONResponse(status_code=500, content=_error_body("internal_error", str(exc)))


@app.exception_handler(RequestValidationError)
async def _handle_validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
    # FastAPI's own 422 for malformed input (e.g. an empty question), remapped
    # to the same {"error", "detail"} shape every other error uses.
    return JSONResponse(
        status_code=422,
        content=_error_body("validation_error", str(exc.errors())),
    )


@app.get("/health")
async def health() -> dict[str, str]:
    """Always public, always 200: used by Docker's HEALTHCHECK and orchestrators."""
    return {"status": "ok"}


@app.post("/ingest", response_model=IngestResponse, dependencies=[Depends(verify_bearer_token)])
async def ingest(request: IngestRequest) -> IngestResponse:
    pipeline: IngestionPipeline = app.state.ingestion_pipeline
    chunk_count = pipeline.ingest_document(
        text=request.text,
        doc_id=request.doc_id,
        source=request.source,
        metadata=request.metadata,
    )
    return IngestResponse(doc_id=request.doc_id, chunk_count=chunk_count)


@app.post("/ask", dependencies=[Depends(verify_bearer_token)])
async def ask(request: AskRequest) -> JSONResponse:
    rag_pipeline: RAGPipeline = app.state.rag_pipeline

    question_hash = hashlib.sha256(request.question.strip().lower().encode("utf-8")).hexdigest()
    start = time.perf_counter()
    result = rag_pipeline.answer(request.question)
    total_latency_ms = round((time.perf_counter() - start) * 1000)

    logger.info(
        "ask: hash=%s cache_hit=%s chunks=%d latency_ms=%d",
        question_hash[:12],
        result.cache_hit,
        len(result.response.citations),
        result.response.latency_ms,
    )

    headers = {"X-Cache-Hit": "true" if result.cache_hit else "false"}
    body = result.response.model_dump()
    # Report the latency actually observed for this request. On a cache hit
    # this is the fast cache-lookup time, not the original slow call's time
    # that was stored alongside the cached answer.
    body["latency_ms"] = total_latency_ms
    return JSONResponse(status_code=200, content=body, headers=headers)
