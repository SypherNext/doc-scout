"""Shared data containers for the Doc Scout research assistant.

This is a first version: plain dataclasses with the default
generated __init__, __repr__, and __eq__. The Magic Methods lesson
later overrides __repr__ and __eq__ with custom versions (a
truncated, readable repr, and equality that ignores fields that
legitimately vary between otherwise-identical runs).
"""
from dataclasses import dataclass, field


@dataclass
class Citation:
    """One supporting excerpt behind part of an answer."""

    source_doc_id: str
    relevance_score: float
    excerpt: str

    def __post_init__(self):
        if not 0.0 <= self.relevance_score <= 1.0:
            raise ValueError(f"relevance_score must be in [0.0, 1.0], got {self.relevance_score}")


@dataclass
class AnswerResponse:
    """A cited answer returned by the RAG pipeline."""

    answer: str
    citations: list[Citation] = field(default_factory=list)
    latency_ms: float = 0.0
