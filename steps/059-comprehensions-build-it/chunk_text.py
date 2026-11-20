# chunk_text.py: the real chunking utility this course has been building toward

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks.

    chunk_size is the maximum length of each chunk. overlap is how many
    characters the end of one chunk shares with the start of the next,
    so content near a chunk boundary is never split without context.
    """
    step = chunk_size - overlap
    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), step)
        if text[i:i + chunk_size].strip()
    ]

from pathlib import Path

def load_documents(docs_dir="data/sample_docs"):
    """Load every .txt file in docs_dir into a list of document records."""
    documents = []
    for path in sorted(Path(docs_dir).glob("*.txt")):
        text = " ".join(path.read_text(encoding="utf-8").split())  # normalize
        documents.append({"doc_id": path.stem, "text": text})
    return documents

documents = load_documents()
for doc in documents:
    chunks = chunk_text(doc["text"], chunk_size=500, overlap=50)
    print(f"{doc['doc_id']}: {len(doc['text'])} characters -> {len(chunks)} chunks")
