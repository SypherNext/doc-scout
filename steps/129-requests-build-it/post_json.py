import requests

# API request to a simulated LLM endpoint
payload = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "What is the capital of France?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100,
}
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json",
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers=headers,
)

print(response.status_code)  # 200

# httpbin echoes the request body
data = response.json()
print(data["json"]["model"])               # gpt-4
print(data["json"]["messages"][0]["content"])  # What is the capital of France?
