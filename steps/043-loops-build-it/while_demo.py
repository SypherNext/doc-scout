# while_demo.py

# Retry loop with exponential backoff
import time

def call_api():
    """Simulated API call that fails sometimes."""
    import random
    return random.choice([True, False])

max_retries = 5
attempt = 1
wait = 1  # seconds

while attempt <= max_retries:
    print(f"Attempt {attempt}/{max_retries}...")
    if call_api():
        print("Success!")
        break
    if attempt < max_retries:
        print(f"Failed, waiting {wait}s...")
        time.sleep(wait)
        wait *= 2  # Exponential backoff: 1, 2, 4, 8 seconds
    attempt += 1
else:
    print("All retries exhausted.")
