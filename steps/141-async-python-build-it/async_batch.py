import asyncio
import time
from http_client import HTTPClient

class AsyncBatchProcessor:
    """Process a batch of items concurrently with rate limiting."""

    def __init__(self, concurrency: int = 10):
        self.client = HTTPClient(base_url="https://httpbin.org")
        self.sem = asyncio.Semaphore(concurrency)
        self.results = []
        self.errors = []

    async def process_one(self, item: dict) -> dict:
        """Process a single item with a real HTTP call."""
        async with self.sem:
            start = time.time()
            response = await self.client.apost(
                "/post", json={"id": item["id"], "complexity": item.get("complexity", 1)}
            )
            response.raise_for_status()
            latency = time.time() - start

            # Injected failure condition: httpbin itself cannot fail on command
            if item.get("should_fail"):
                raise ValueError(f"Item {item['id']} failed processing")

            return {
                "id": item["id"],
                "result": f"Processed in {latency:.2f}s",
                "latency": latency,
            }

    async def run_batch(self, items: list[dict]) -> dict:
        """Process all items concurrently."""
        start = time.time()

        async def safe_process(item: dict):
            try:
                result = await self.process_one(item)
                self.results.append(result)
            except Exception as e:
                self.errors.append({"id": item["id"], "error": str(e)})

        tasks = [safe_process(item) for item in items]
        await asyncio.gather(*tasks)

        elapsed = time.time() - start
        return {
            "total": len(items),
            "success": len(self.results),
            "failed": len(self.errors),
            "elapsed_seconds": round(elapsed, 2),
            "avg_latency": round(
                sum(r["latency"] for r in self.results) / max(len(self.results), 1),
                2,
            ),
        }

async def main():
    # Create a batch of 20 items; every 7th one is flagged to fail
    items = [
        {"id": i, "complexity": (i % 3) + 1, "should_fail": (i % 7 == 0)}
        for i in range(20)
    ]

    processor = AsyncBatchProcessor(concurrency=5)
    summary = await processor.run_batch(items)

    print(f"Batch Summary:")
    print(f"  Total:    {summary['total']}")
    print(f"  Success:  {summary['success']}")
    print(f"  Failed:   {summary['failed']}")
    print(f"  Elapsed:  {summary['elapsed_seconds']}s")
    print(f"  Avg lat:  {summary['avg_latency']}s")

    # Expected: at minimum, ids 0, 7, 14 fail (the injected ValueError),
    # so success should be at most 17/20. Elapsed time depends on real
    # network latency to httpbin, not a fixed number: with 5 concurrent
    # slots, expect roughly 4 batches worth of round-trip time rather
    # than 20x a single request's time.

asyncio.run(main())
