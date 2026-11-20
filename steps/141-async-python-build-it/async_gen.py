import asyncio

async def stream_tokens(text: str):
    """Simulate streaming tokens one at a time."""
    for word in text.split():
        await asyncio.sleep(0.2)  # Simulate network delay per token
        yield word

async def main():
    prompt = "Async Python makes concurrent programming elegant"
    print("Streaming tokens:")
    async for token in stream_tokens(prompt):
        print(f"  Received: {token}")

asyncio.run(main())
