import asyncio

async def background_worker(name: str, interval: float):
    """Run indefinitely, doing periodic work."""
    for i in range(5):
        await asyncio.sleep(interval)
        print(f"  [{name}] Tick {i + 1}")
    return f"{name} done"

async def main():
    # Start background tasks: they run in the background
    task1 = asyncio.create_task(background_worker("worker-A", 0.5))
    task2 = asyncio.create_task(background_worker("worker-B", 0.8))

    # Do main work while background tasks run
    print("Main: Starting main work...")
    for i in range(3):
        await asyncio.sleep(1.0)
        print(f"Main: Working... step {i + 1}")
    print("Main: Main work complete.")

    # Wait for background tasks to finish
    result1 = await task1
    result2 = await task2
    print(f"Results: {result1}, {result2}")

asyncio.run(main())
