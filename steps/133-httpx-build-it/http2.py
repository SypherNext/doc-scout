import httpx

# Enable HTTP/2 support
with httpx.Client(http2=True) as client:
    response = client.get("https://httpbin.org/get")
    print(f"HTTP version: {response.http_version}")  # HTTP/2 or HTTP/1.1

# With async
import asyncio

async def http2_async():
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get("https://httpbin.org/get")
        print(f"Async HTTP version: {response.http_version}")

asyncio.run(http2_async())
