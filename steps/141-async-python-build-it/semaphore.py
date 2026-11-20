import asyncio
from http_client import HTTPClient

client = HTTPClient(base_url="https://httpbin.org")

async def call_api(session_id: int) -> str:
    """Make a real HTTP call to an endpoint that delays ~1 second."""
    response = await client.aget("/delay/1")
    return f"Session {session_id} complete (status {response.status_code})"

async def main():
    sem = asyncio.Semaphore(5)  # Max 5 concurrent calls

    async def limited_call(session_id: int) -> str:
        async with sem:
            return await call_api(session_id)

    # Create 20 tasks
    tasks = [limited_call(i) for i in range(20)]

    start = asyncio.get_event_loop().time()
    results = await asyncio.gather(*tasks)
    elapsed = asyncio.get_event_loop().time() - start

    print(f"Completed {len(results)} tasks with concurrency 5 in {elapsed:.1f}s")
    # With 20 real calls at concurrency 5, expect roughly 20/5 = 4 batches
    # of ~1s server-side delay each, plus real network overhead: ~4-6s total.

asyncio.run(main())
