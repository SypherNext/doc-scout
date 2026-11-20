import asyncio

async def some_coroutine():
    await asyncio.sleep(0.1)
    return "done"

# This line itself works fine in a plain script (there is no event loop
# running yet). The error below only happens inside an environment that
# already has one running, like a Jupyter cell:
asyncio.run(some_coroutine())  # In Jupyter: raises RuntimeError


# await some_coroutine()
