import httpx
import asyncio

async def main():
    client = httpx.AsyncClient()
    # Wrong: missing await
    response = client.get("https://httpbin.org/get")
    # This returns a Coroutine, not a Response!

    # Correct
    response = await client.get("https://httpbin.org/get")
    await client.aclose()

asyncio.run(main())
