import requests

# Without a session: each request opens a new connection
for _ in range(5):
    requests.get("https://httpbin.org/get")

# With a session: connections are reused (faster)
with requests.Session() as session:
    # Set default headers for all requests through this session
    session.headers.update({
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
    })

    for model in ["gpt-4", "claude-3", "llama-3"]:
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": "Hello"}],
        }
        response = session.post("https://httpbin.org/post", json=payload)
        print(f"{model}: {response.status_code}")
