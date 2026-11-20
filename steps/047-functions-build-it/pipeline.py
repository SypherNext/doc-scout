# pipeline.py: A reusable data processing pipeline using functions

def load_texts(file_paths: list[str]) -> list[str]:
    """Load text content from multiple files."""
    texts = []
    for path in file_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                texts.append(f.read())
        except FileNotFoundError:
            print(f"Warning: {path} not found, skipping.")
    return texts

def clean_text(text: str) -> str:
    """Basic text cleaning for AI input."""
    text = text.strip()
    text = text.replace("\n", " ")
    # Remove extra whitespace
    import re
    text = re.sub(r"\s+", " ", text)
    return text

def split_into_blocks(text: str, max_chars: int = 1000) -> list[str]:
    """Split text into fixed-size, non-overlapping blocks for model input.

    This is a first pass: it has no overlap between blocks, so a sentence
    sitting on a block boundary gets cut in two. Comprehensions, later in
    this course, builds the overlapping version used for real retrieval.
    """
    blocks = []
    for i in range(0, len(text), max_chars):
        block = text[i:i + max_chars]
        blocks.append(block)
    return blocks

def run_pipeline(file_paths: list[str]) -> list[str]:
    """Run the full pipeline: load -> clean -> split into blocks."""
    texts = load_texts(file_paths)
    all_blocks = []

    for text in texts:
        text = clean_text(text)
        blocks = split_into_blocks(text, max_chars=1000)
        all_blocks.extend(blocks)

    return all_blocks

# This would run on the sample document collection from File Handling:
# blocks = run_pipeline(["data/sample_docs/caching-strategies.txt", "data/sample_docs/load-balancing.txt"])
# print(f"Generated {len(blocks)} blocks for model input")
