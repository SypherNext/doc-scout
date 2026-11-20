import asyncio

async def might_fail(item_id: int):
    if item_id == 2:
        raise ValueError(f"Item {item_id} failed")
    await asyncio.sleep(0.5)
    return f"Item {item_id} OK"

async def main():
    # If any task raises, gather propagates the first exception
    try:
        results = await asyncio.gather(
            might_fail(1),
            might_fail(2),  # This raises
            might_fail(3),
        )
    except ValueError as e:
        print(f"gather() raised and the other results are lost: {e}")

asyncio.run(main())  # prints: gather() raised and the other results are lost: Item 2 failed


async def main_fixed():
    results = await asyncio.gather(
        might_fail(1),
        might_fail(2),
        might_fail(3),
        return_exceptions=True,
    )
    # results = ["Item 1 OK", ValueError("Item 2 failed"), "Item 3 OK"]
    for r in results:
        if isinstance(r, Exception):
            print(f"Task failed: {r}")
        else:
            print(f"Success: {r}")

asyncio.run(main_fixed())
