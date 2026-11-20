import os
import requests

# Load from environment, never hardcode
API_KEY = os.environ.get("OPENAI_API_KEY", "sk-test-placeholder")

# API key in header (most common)
headers = {
    "Authorization": f"Bearer {API_KEY}",
}
response = requests.get(
    "https://httpbin.org/headers",
    headers=headers,
    timeout=10,
)
print(response.json()["headers"]["Authorization"])  # Bearer sk-test-...

# Or API key in a custom header
headers = {"X-API-Key": API_KEY}
response = requests.get(
    "https://httpbin.org/headers",
    headers=headers,
    timeout=10,
)
