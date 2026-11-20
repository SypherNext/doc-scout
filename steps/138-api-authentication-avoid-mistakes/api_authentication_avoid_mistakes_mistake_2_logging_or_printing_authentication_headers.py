import requests

API_KEY = "sk-test-placeholder"
url = "https://httpbin.org/get"

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, headers=headers)

# Wrong, prints the key to logs!
print(f"Request headers: {response.request.headers}")
print(f"Response: {response.json()}")


safe_headers = {
    k: (v[:8] + "..." if k.lower() == "authorization" else v)
    for k, v in response.request.headers.items()
}
print(f"Request headers: {safe_headers}")
