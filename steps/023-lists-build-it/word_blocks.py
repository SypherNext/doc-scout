# word_blocks.py

def split_into_word_blocks(text, words_per_block=40):
    """Split normalized text into a list of word blocks."""
    words = text.split()
    blocks = []
    for i in range(0, len(words), words_per_block):
        block_words = words[i:i + words_per_block]
        blocks.append(" ".join(block_words))
    return blocks

document = (
    "A cache stores a copy of data that is expensive to produce so that a "
    "later request can be served quickly from the copy instead of redoing "
    "the expensive work. The classic motivating example is a database query."
)

blocks = split_into_word_blocks(document, words_per_block=15)
print(f"Split into {len(blocks)} blocks")
for i, block in enumerate(blocks):
    print(f"Block {i}: {block}")
