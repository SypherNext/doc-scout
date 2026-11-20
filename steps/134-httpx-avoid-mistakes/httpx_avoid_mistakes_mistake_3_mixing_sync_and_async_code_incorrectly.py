import asyncio
import httpx

async def fetch():
    async with httpx.AsyncClient() as client:
        return await client.get("https://httpbin.org/get")

# Wrong in a script that is already running an event loop (e.g. Jupyter):
asyncio.run(fetch())
# RuntimeError: asyncio.run() cannot be called from a running event loop
