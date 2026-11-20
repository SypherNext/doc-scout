import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/json")
        print(response.status_code)  # 200
        data = response.json()
        print(data["slideshow"]["title"])

        # POST with JSON
        payload = {
            "model": "gpt-4",
            "messages": [{"role": "user", "content": "Hello"}],
        }
        response = await client.post(
            "https://httpbin.org/post",
            json=payload,
            timeout=10,
        )
        print(f"Posted: {response.status_code}")

asyncio.run(main())
