import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

async def main():
    # Wrong: creates a coroutine object but never runs it
    result = fetch_data()
    print(result)  # <coroutine object fetch_data at 0x...>

    # Correct
    result = await fetch_data()
    print(result)  # data

asyncio.run(main())
