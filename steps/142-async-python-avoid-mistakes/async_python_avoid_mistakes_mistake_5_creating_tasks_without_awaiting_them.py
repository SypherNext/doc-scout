import asyncio

async def worker():
    await asyncio.sleep(1)
    print("Worker done")

async def main():
    # Task is created but never awaited: it may not complete
    asyncio.create_task(worker())

    # Without await, the event loop shuts down immediately
    # "Worker done" may not print

asyncio.run(main())


async def main():
    task = asyncio.create_task(worker())
    # ... do other work ...
    await task  # Wait for the task to finish
