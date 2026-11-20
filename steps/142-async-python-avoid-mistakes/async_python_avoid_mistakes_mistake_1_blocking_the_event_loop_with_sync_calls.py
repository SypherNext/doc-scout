import asyncio
import time

async def main():
    # This blocks the ENTIRE event loop: no other coroutine can run
    time.sleep(2)  # Blocking call!
    print("Done")

# Compare with:
async def main():
    await asyncio.sleep(2)  # Non-blocking: yields to event loop
    print("Done")


import asyncio
import time

def slow_sync_function(n: float) -> str:
    time.sleep(n)  # a blocking call you cannot easily rewrite as async
    return f"done after {n}s"

async def main():
    # Runs the blocking call in a thread pool instead of the event loop
    result = await asyncio.to_thread(slow_sync_function, 1)
    print(result)

asyncio.run(main())
