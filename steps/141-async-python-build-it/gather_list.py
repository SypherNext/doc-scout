import asyncio
from http_client import HTTPClient

client = HTTPClient(base_url="https://httpbin.org")

async def process_prompt(prompt: str) -> str:
    """Send a prompt to httpbin and read back what it echoed."""
    response = await client.apost("/post", json={"prompt": prompt})
    echoed = response.json()["json"]["prompt"]
    return f"Echoed: {echoed[:20]}..."

async def main():
    prompts = [
        "What is Python?",
        "Explain async/await.",
        "How does list comprehension work?",
        "What is the difference between a list and a tuple?",
        "Explain NumPy broadcasting.",
    ]

    # Create a coroutine for each prompt
    tasks = [process_prompt(p) for p in prompts]

    # Run all concurrently
    results = await asyncio.gather(*tasks)

    for prompt, result in zip(prompts, results):
        print(f"{prompt[:25]:25s} → {result}")

asyncio.run(main())
