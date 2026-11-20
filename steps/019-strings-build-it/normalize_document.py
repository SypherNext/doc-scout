# normalize_document.py

def normalize_document_text(raw_text):
    """Collapse whitespace and strip a raw document's text to one clean string."""
    # Treat any run of whitespace (spaces, tabs, newlines) as a single space
    words = raw_text.split()
    return " ".join(words)

raw = """  Caching Strategies

    A cache stores a copy of data   that is expensive to produce
  so that a later request   can be served quickly.
"""

cleaned = normalize_document_text(raw)
print(cleaned)
# Caching Strategies A cache stores a copy of data that is expensive to produce so that a later request can be served quickly.
print(f"Raw length: {len(raw)}, cleaned length: {len(cleaned)}")
