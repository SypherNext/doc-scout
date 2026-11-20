"""Pydantic request/response schemas for the research assistant API.

``Citation`` and ``AnswerResponse`` are listed in the shared repo spec as
dataclasses Course 2 builds. Course 2's module was not present when this
app/ was built, so these are defined here as Pydantic models (not plain
dataclasses) because they double as the API's response schema and as the
JSON schema handed to Anthropic's tool-use for forced structured output
(``AnswerResponse.model_json_schema()`` / a trimmed version of it -- see
``rag/generator.py``). If Course 2 lands plain dataclasses with the same
field names, prefer theirs for internal pipeline state and keep a thin
Pydantic wrapper here only for the HTTP boundary.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class Citation(BaseModel):
    """One retrieved-and-cited source chunk backing an answer."""

    source_doc_id: str = Field(
        description="doc_id of the ingested document this citation came from"
    )
    relevance_score: float = Field(
        description="Cosine similarity of the chunk to the question, 0-1"
    )


class AnswerResponse(BaseModel):
    """The shape every successful ``POST /ask`` response conforms to."""

    answer: str
    citations: list[Citation] = Field(default_factory=list)
    latency_ms: int


class AskRequest(BaseModel):
    """Body of ``POST /ask``."""

    question: str = Field(min_length=1, max_length=2000)


class IngestRequest(BaseModel):
    """Body of ``POST /ingest``."""

    doc_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    source: str | None = None
    metadata: dict[str, str] | None = None


class IngestResponse(BaseModel):
    """Response of ``POST /ingest``."""

    doc_id: str
    chunk_count: int


class ErrorResponse(BaseModel):
    """The structured JSON body returned for every error, of every kind."""

    error: str
    detail: str
