# document_loader.py: Load every document in the sample collection

from pathlib import Path

def load_documents(docs_dir="data/sample_docs"):
    """Load every .txt file in docs_dir into a list of document records."""
    documents = []
    for path in sorted(Path(docs_dir).glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        documents.append({"doc_id": path.stem, "text": text})
    return documents

documents = load_documents()
print(f"Loaded {len(documents)} documents")
for doc in documents:
    word_count = len(doc["text"].split())
    print(f"  {doc['doc_id']}: {word_count} words")
