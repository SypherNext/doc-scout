import httpx
import asyncio

async def fetch_model(client, model_name):
    """Send a single model inference request."""
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": "Hello world"}],
    }
    response = await client.post(
        "https://httpbin.org/post",
        json=payload,
        timeout=30,
    )
    return model_name, response.status_code

async def main():
    models = ["gpt-4", "claude-3", "llama-3", "gemini", "mistral"]

    async with httpx.AsyncClient() as client:
        # Create concurrent tasks
        tasks = [fetch_model(client, m) for m in models]

        # Run all tasks concurrently
        results = await asyncio.gather(*tasks)

        for model, status in results:
            print(f"{model}: {status}")

asyncio.run(main())
