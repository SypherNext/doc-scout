"""Generate a grounded, cited answer from retrieved context.

Uses Anthropic tool-use with a forced ``tool_choice`` (the Structured Output
lesson's pattern) so the model always returns JSON matching the answer
schema: no markdown-fenced JSON to regex out, no "sometimes free text"
ambiguity.

The tool's ``input_schema`` is written by hand rather than generated with
``AnswerResponse.model_json_schema()``, to sidestep the Reference
Architecture's pitfall #3: Pydantic v2 emits ``$defs``/``$ref`` for nested
models (``Citation``), and the schema is simple enough that inlining it
avoids that pitfall entirely rather than working around it.
"""

from __future__ import annotations

from typing import Any

from research_assistant.llm.clients import AnthropicClient
from research_assistant.models import AnswerResponse, Citation
from research_assistant.rag.retriever import RetrievedChunk

TOOL_NAME = "answer_question"

NO_CONTEXT_MESSAGE = (
    "No relevant documents were found for this question. "
    "Ingest a document that covers this topic and try again."
)

_ANSWER_TOOL_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "description": "The answer to the question, grounded only in the provided context.",
        },
        "citations": {
            "type": "array",
            "description": "One entry per context passage actually used to answer the question.",
            "items": {
                "type": "object",
                "properties": {
                    "source_doc_id": {"type": "string"},
                    "relevance_score": {"type": "number"},
                },
                "required": ["source_doc_id", "relevance_score"],
            },
        },
    },
    "required": ["answer", "citations"],
}

_SYSTEM_PROMPT = (
    "You are a research assistant that answers questions using only the "
    "context passages provided. Cite every passage you actually used by "
    "its document id. If the context does not contain enough information "
    "to answer, say so plainly in the answer field and return an empty "
    "citations list. Never use outside knowledge or invent citations."
)


class Generator:
    """Wraps an Anthropic client to produce a structured, cited answer."""

    def __init__(self, llm_client: AnthropicClient) -> None:
        self._llm_client = llm_client

    def generate_answer(self, question: str, chunks: list[RetrievedChunk]) -> AnswerResponse:
        """Produce a grounded answer from retrieved chunks.

        Args:
            question: The user's question.
            chunks: Chunks returned by :meth:`Retriever.query`. If empty,
                the LLM is never called: a fixed no-context message is
                returned instead, per the Capstone's "never hallucinate"
                requirement.

        Returns:
            An ``AnswerResponse`` with ``latency_ms`` left at 0: the caller
            (``RAGPipeline``) fills in end-to-end timing.
        """
        if not chunks:
            return AnswerResponse(answer=NO_CONTEXT_MESSAGE, citations=[], latency_ms=0)

        context = "\n\n".join(f"[{chunk.doc_id}] {chunk.document}" for chunk in chunks)
        messages = [
            {
                "role": "user",
                "content": (
                    f"Context:\n{context}\n\n"
                    f"Question: {question}\n\n"
                    "Answer using only the context above, and cite the document "
                    "ids of every passage you used."
                ),
            }
        ]

        raw = self._llm_client.generate_structured(
            messages=messages,
            tool_name=TOOL_NAME,
            tool_schema=_ANSWER_TOOL_SCHEMA,
            tool_description="Return the grounded answer and its citations.",
            system=_SYSTEM_PROMPT,
        )

        citations = [
            Citation(
                source_doc_id=item["source_doc_id"],
                relevance_score=float(item["relevance_score"]),
            )
            for item in raw.get("citations", [])
        ]
        return AnswerResponse(answer=raw["answer"], citations=citations, latency_ms=0)
