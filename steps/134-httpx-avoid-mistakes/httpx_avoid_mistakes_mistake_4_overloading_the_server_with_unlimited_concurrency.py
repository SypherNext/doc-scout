import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        # Sends 1000 requests at once: likely to overwhelm both client and server
        tasks = [client.get("https://api.example.com") for _ in range(1000)]
        results = await asyncio.gather(*tasks)


sem = asyncio.Semaphore(10)  # Max 10 concurrent requests

async def limited_request(client, url):
    async with sem:
        return await client.get(url)
