import httpx

# Stream response content (for large downloads)
with httpx.Client() as client:
    with client.stream("GET", "https://httpbin.org/stream/5") as response:
        for line in response.iter_lines():
            if line:
                print(line)  # httpx.Response.iter_lines() already yields str, not bytes

# Async streaming (for LLM token streaming)
import asyncio

async def stream_async():
    async with httpx.AsyncClient() as client:
        async with client.stream(
            "GET",
            "https://httpbin.org/stream/3",
        ) as response:
            async for line in response.aiter_lines():
                if line:
                    print(f"Chunk: {line}")

asyncio.run(stream_async())
