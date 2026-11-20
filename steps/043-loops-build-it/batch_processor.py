# batch_processor.py: Process a batch of inputs with progress tracking

import time

def mock_inference(text):
    """Simulate LLM inference."""
    time.sleep(0.1)  # Simulate latency
    return {"input": text, "tokens": len(text.split()), "sentiment": "positive"}

def process_batch(inputs, batch_size=5):
    """Process inputs in batches with progress reporting."""
    results = []
    total = len(inputs)

    for i in range(0, total, batch_size):
        batch = inputs[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (total + batch_size - 1) // batch_size
        print(f"Batch {batch_num}/{total_batches} ({i+1}-{min(i+batch_size, total)} of {total})")

        for item in batch:
            result = mock_inference(item)
            results.append(result)

    return results

inputs = [
    "This product is amazing",
    "Not what I expected",
    "Decent quality for the price",
    "Customer support was unhelpful",
    "Would recommend to a friend",
    "Average at best",
    "Exceeded my expectations",
    "Needs improvement",
    "Perfect for daily use",
    "Could be better",
]

results = process_batch(inputs, batch_size=3)
print(f"\nProcessed {len(results)} inputs")

# Count tokens efficiently
total_tokens = sum(r["tokens"] for r in results)
print(f"Total tokens processed: {total_tokens}")
