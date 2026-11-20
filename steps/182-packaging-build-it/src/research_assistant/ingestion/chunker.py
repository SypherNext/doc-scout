"""Split documents into overlapping, token-aligned chunks for embedding.

This is the production version of the RAG lesson's teaching chunker: same
name and signature and the same defaults the lesson and the Capstone
Requirements both use, ``chunk_size=500, chunk_overlap=100`` (the top-level
shared repo spec that kicked off this build listed a default overlap of 50;
that is superseded here by the course's own lesson text and Capstone
Requirements, which are explicit about 500/100 -- noted as a spec conflict
in the integration report). Guards are added for edge cases the teaching
version does not need to handle: empty text, and an overlap that is not
smaller than the chunk size (which would otherwise loop forever, since
``start`` would never advance).
"""

from __future__ import annotations

import tiktoken

DEFAULT_CHUNK_SIZE = 500
DEFAULT_CHUNK_OVERLAP = 100
DEFAULT_ENCODING = "cl100k_base"


def chunk_text(
    text: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    encoding_name: str = DEFAULT_ENCODING,
) -> list[str]:
    """Split text into overlapping token-aligned chunks.

    Args:
        text: The full document text. An empty or whitespace-only string
            produces zero chunks rather than raising, so ingestion of an
            empty document can return a clean "0 chunks" response instead
            of crashing.
        chunk_size: Target tokens per chunk.
        chunk_overlap: Tokens of overlap between adjacent chunks. Must be
            strictly smaller than ``chunk_size``.
        encoding_name: Tokeniser matching your embedding model.

    Returns:
        List of text chunks, in document order.

    Raises:
        ValueError: If ``chunk_overlap >= chunk_size``, which would make
            the sliding window stop advancing.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError(
            f"chunk_overlap ({chunk_overlap}) must be smaller than chunk_size ({chunk_size})"
        )

    if not text or not text.strip():
        return []

    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)

    chunks: list[str] = []
    start = 0
    stride = chunk_size - chunk_overlap
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunks.append(encoding.decode(chunk_tokens))
        start += stride

    return chunks
