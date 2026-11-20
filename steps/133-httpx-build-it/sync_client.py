import httpx

# Basic GET
response = httpx.get("https://httpbin.org/json")
print(response.status_code)   # 200
print(response.json()["slideshow"]["title"])  # Sample Slide Show

# POST with JSON
payload = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}],
}
response = httpx.post(
    "https://httpbin.org/post",
    json=payload,
    timeout=10,
)
print(response.status_code)  # 200

# Using a Client for connection reuse
with httpx.Client() as client:
    client.headers.update({"Authorization": "Bearer test-key"})
    for model in ["gpt-4", "claude-3", "llama-3"]:
        r = client.post(
            "https://httpbin.org/post",
            json={"model": model, "prompt": "Hi"},
        )
        print(f"{model}: {r.status_code}")
