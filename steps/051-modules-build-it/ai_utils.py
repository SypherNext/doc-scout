# ai_utils.py: Your own reusable module

def split_fixed_width(text, max_chars=1000):
    """Split text into fixed-width, non-overlapping blocks.

    This moves the split_into_blocks() helper from the Functions lesson
    into its own module so any script can import and reuse it. It is
    still a first pass: no overlap between blocks yet. Comprehensions,
    later in this course, upgrades this into a real chunk_text() with
    overlap, which is what the sample documents get split with.
    """
    blocks = []
    for i in range(0, len(text), max_chars):
        blocks.append(text[i:i + max_chars])
    return blocks

def count_tokens(text):
    """Approximate token count (4 characters ≈ 1 token)."""
    return len(text) // 4

def truncate_to_max_tokens(text, max_tokens):
    """Truncate text to a maximum number of approximate tokens."""
    max_chars = max_tokens * 4
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
