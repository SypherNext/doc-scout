"""Shared data containers for the Doc Scout research assistant.

Citation and AnswerResponse are dataclasses: plain data with a small
amount of custom behaviour layered on top (see __repr__ and __eq__
below, which override the dataclass-generated versions).
"""
from dataclasses import dataclass, field


@dataclass(repr=False, eq=False)
class Citation:
    """One supporting excerpt behind part of an answer."""

    source_doc_id: str
    relevance_score: float
    excerpt: str

    def __repr__(self) -> str:
        """Shortened, developer-facing representation: truncate the excerpt
        so a list of citations doesn't flood the console or the logs."""
        preview = self.excerpt[:40] + ("..." if len(self.excerpt) > 40 else "")
        return (
            f"Citation(source_doc_id={self.source_doc_id!r}, "
            f"relevance_score={self.relevance_score:.3f}, excerpt={preview!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Two citations are equal if they point at the same document and
        excerpt. relevance_score is deliberately excluded: the same quote
        can be re-ranked slightly differently between runs without making
        it a different citation."""
        if not isinstance(other, Citation):
            return NotImplemented
        return (
            self.source_doc_id == other.source_doc_id
            and self.excerpt == other.excerpt
        )

    def __hash__(self) -> int:
        return hash((self.source_doc_id, self.excerpt))


@dataclass(repr=False, eq=False)
class AnswerResponse:
    """A cited answer returned by the RAG pipeline."""

    answer: str
    citations: list[Citation] = field(default_factory=list)
    latency_ms: float = 0.0

    def __repr__(self) -> str:
        preview = self.answer[:50] + ("..." if len(self.answer) > 50 else "")
        return (
            f"AnswerResponse(answer={preview!r}, "
            f"citations={len(self.citations)}, latency_ms={self.latency_ms:.1f})"
        )

    def __eq__(self, other: object) -> bool:
        """Two answers are equal if the text and citations match. latency_ms
        is excluded: timing varies between runs even for an identical
        answer, and callers comparing responses (e.g. in tests, or the
        query cache) care about content, not how long it took."""
        if not isinstance(other, AnswerResponse):
            return NotImplemented
        return self.answer == other.answer and self.citations == other.citations
