"""Tests for research_assistant.rag.pipeline.RAGPipeline."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from research_assistant.cache import QueryCache
from research_assistant.models import AnswerResponse
from research_assistant.rag.pipeline import RAGPipeline


@pytest.fixture
def mock_retriever() -> MagicMock:
    retriever = MagicMock()
    retriever.query.return_value = []
    return retriever


@pytest.fixture
def mock_generator() -> MagicMock:
    generator = MagicMock()
    generator.generate_answer.return_value = AnswerResponse(
        answer="Python is a programming language.",
        citations=[],
        latency_ms=0,
    )
    return generator


@pytest.fixture
def pipeline(
    mock_retriever: MagicMock, mock_generator: MagicMock, query_cache: QueryCache
) -> RAGPipeline:
    return RAGPipeline(
        retriever=mock_retriever, generator=mock_generator, cache=query_cache, top_k=3
    )


def test_first_call_is_a_cache_miss(pipeline: RAGPipeline, mock_generator: MagicMock) -> None:
    result = pipeline.answer("What is Python?")

    assert result.cache_hit is False
    assert result.response.answer == "Python is a programming language."
    mock_generator.generate_answer.assert_called_once()


def test_second_identical_call_is_a_cache_hit(
    pipeline: RAGPipeline, mock_generator: MagicMock
) -> None:
    pipeline.answer("What is Python?")
    result = pipeline.answer("What is Python?")

    assert result.cache_hit is True
    assert result.response.answer == "Python is a programming language."
    # The generator is only invoked once: the second call never reaches it.
    mock_generator.generate_answer.assert_called_once()


@pytest.mark.parametrize(
    "first_question, second_question",
    [
        ("What is Python?", "WHAT IS PYTHON?"),
        ("  What is Python?  ", "What is Python?"),
    ],
)
def test_cache_hit_is_case_and_whitespace_insensitive(
    pipeline: RAGPipeline, mock_generator: MagicMock, first_question: str, second_question: str
) -> None:
    pipeline.answer(first_question)
    result = pipeline.answer(second_question)

    assert result.cache_hit is True
    mock_generator.generate_answer.assert_called_once()


def test_different_questions_are_different_cache_entries(
    pipeline: RAGPipeline, mock_generator: MagicMock
) -> None:
    pipeline.answer("What is Python?")
    result = pipeline.answer("What is Rust?")

    assert result.cache_hit is False
    assert mock_generator.generate_answer.call_count == 2


def test_pipeline_passes_top_k_to_retriever(
    pipeline: RAGPipeline, mock_retriever: MagicMock
) -> None:
    pipeline.answer("A new question")
    mock_retriever.query.assert_called_once_with("A new question", top_k=3)
