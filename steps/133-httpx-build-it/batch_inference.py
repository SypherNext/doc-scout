import asyncio
import time
from http_client import HTTPClient

async def main():
    prompts = [
        "What is Python?",
        "Explain list comprehensions.",
        "What is the difference between a list and a tuple?",
        "How does async/await work?",
        "What is NumPy used for?",
    ]

    client = HTTPClient(base_url="https://httpbin.org")
    requests_spec = [
        ("POST", "/post", {"model": "gpt-4", "messages": [{"role": "user", "content": p}]})
        for p in prompts
    ]

    start = time.time()
    results = await client.run_concurrent(requests_spec, max_concurrent=5)
    elapsed = time.time() - start

    success_count = sum(1 for r in results if not isinstance(r, Exception))
    print(f"Completed {success_count}/{len(prompts)} in {elapsed:.2f}s")
    for i, r in enumerate(results):
        status = "OK" if not isinstance(r, Exception) else f"FAIL: {r}"
        print(f"  [{i}] {status}")

asyncio.run(main())
