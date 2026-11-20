"""Tests for research_assistant.ingestion.chunker.chunk_text."""

from __future__ import annotations

import pytest

from research_assistant.ingestion.chunker import chunk_text


def test_empty_text_returns_no_chunks() -> None:
    assert chunk_text("") == []


def test_whitespace_only_text_returns_no_chunks() -> None:
    assert chunk_text("   \n\t  ") == []


def test_short_text_returns_one_chunk() -> None:
    chunks = chunk_text("Python is a programming language.", chunk_size=100, chunk_overlap=10)
    assert len(chunks) == 1
    assert "Python" in chunks[0]


def test_long_text_produces_overlapping_chunks() -> None:
    text = " ".join(f"word{i}" for i in range(400))
    chunks = chunk_text(text, chunk_size=50, chunk_overlap=10)

    assert len(chunks) > 1
    # The end of one chunk and the start of the next share overlapping content.
    assert chunks[0].strip().split()[-1] in chunks[1]


def test_chunk_overlap_must_be_smaller_than_chunk_size() -> None:
    with pytest.raises(ValueError):
        chunk_text("some text", chunk_size=50, chunk_overlap=50)


def test_chunk_overlap_larger_than_chunk_size_raises() -> None:
    with pytest.raises(ValueError):
        chunk_text("some text", chunk_size=50, chunk_overlap=60)


def test_default_chunk_size_and_overlap_match_the_course_spec() -> None:
    # The RAG lesson and Capstone Requirements both specify 500/100.
    chunks = chunk_text("word " * 1000)
    assert len(chunks) > 1
