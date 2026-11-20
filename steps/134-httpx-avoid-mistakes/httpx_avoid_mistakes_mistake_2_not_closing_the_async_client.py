import httpx
import asyncio

async def main():
    client = httpx.AsyncClient()
    await client.get("https://httpbin.org/get")
    # Client is never closed: connections leak!

asyncio.run(main())


import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")

asyncio.run(main())
