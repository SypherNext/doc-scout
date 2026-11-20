def chunk_text(text, chunk_size=500, overlap=50):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    step = chunk_size - overlap
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), step)
        if text[i:i + chunk_size].strip()
    ]
