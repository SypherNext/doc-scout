"""Tests for research_assistant.rag.generator.Generator."""

from __future__ import annotations

from research_assistant.rag.generator import NO_CONTEXT_MESSAGE, Generator
from research_assistant.rag.retriever import RetrievedChunk


def test_generate_answer_with_no_chunks_never_calls_the_llm(generator: Generator) -> None:
    response = generator.generate_answer("What is Python?", chunks=[])

    assert response.answer == NO_CONTEXT_MESSAGE
    assert response.citations == []
    generator._llm_client.generate_structured.assert_not_called()


def test_generate_answer_returns_structured_citations(generator: Generator) -> None:
    chunks = [
        RetrievedChunk(
            document="Python was created by Guido van Rossum.",
            doc_id="python_intro",
            score=0.91,
            metadata={"doc_id": "python_intro"},
        )
    ]

    response = generator.generate_answer("Who created Python?", chunks=chunks)

    assert response.answer == "Python was created by Guido van Rossum."
    assert len(response.citations) == 1
    assert response.citations[0].source_doc_id == "python_intro"
    assert response.citations[0].relevance_score == 0.91


def test_generate_answer_passes_context_from_all_chunks(generator: Generator) -> None:
    chunks = [
        RetrievedChunk(document="Fact one.", doc_id="doc1", score=0.9, metadata={}),
        RetrievedChunk(document="Fact two.", doc_id="doc2", score=0.8, metadata={}),
    ]

    generator.generate_answer("A question", chunks=chunks)

    call_kwargs = generator._llm_client.generate_structured.call_args.kwargs
    prompt = call_kwargs["messages"][0]["content"]
    assert "Fact one." in prompt
    assert "Fact two." in prompt
    assert "[doc1]" in prompt
    assert "[doc2]" in prompt
