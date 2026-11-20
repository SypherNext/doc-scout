import asyncio
import time
from http_client import HTTPClient

client = HTTPClient(base_url="https://httpbin.org")

async def fetch_data(item_id: int) -> str:
    """Make a real HTTP call to an endpoint that delays ~1 second."""
    response = await client.aget("/delay/1")
    return f"Data for item {item_id} (status {response.status_code})"

async def sequential():
    """Run tasks one at a time: total ~3 seconds."""
    start = time.time()
    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    result3 = await fetch_data(3)
    elapsed = time.time() - start
    print(f"Sequential: {result1}, {result2}, {result3} ({elapsed:.1f}s)")

async def concurrent():
    """Run tasks concurrently: total ~1 second."""
    start = time.time()
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
    )
    elapsed = time.time() - start
    print(f"Concurrent: {results} ({elapsed:.1f}s)")

asyncio.run(sequential())  # ~3 seconds, plus real network latency
asyncio.run(concurrent())  # ~1 second, plus real network latency
