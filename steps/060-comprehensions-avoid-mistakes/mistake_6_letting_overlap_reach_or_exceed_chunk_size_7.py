def chunk_text(text, chunk_size=500, overlap=50):
    step = chunk_size - overlap
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), step)
        if text[i:i + chunk_size].strip()
    ]

chunk_text("some long document text here", chunk_size=100, overlap=100)
# ValueError: range() arg 3 must not be zero
# step = 100 - 100 = 0, and range() refuses a step of exactly 0

chunk_text("some long document text here", chunk_size=100, overlap=150)
# []  -- silently returns zero chunks, no error at all
# step = 100 - 150 = -5, and range(0, len(text), -5) with len(text) > 0
# produces no values at all: an empty range, not an infinite loop
