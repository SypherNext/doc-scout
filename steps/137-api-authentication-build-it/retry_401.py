from http_client import HTTPClient

def fetch_token() -> tuple[str, int]:
    return "sk-fresh-token", 3600

client = HTTPClient(base_url="https://httpbin.org", token_provider=fetch_token)

# httpbin's /status/401 endpoint always returns 401 regardless of auth,
# which makes it useful for observing the retry-once behavior directly.
response = client.get("/status/401")
print(f"Status after one retry attempt: {response.status_code}")
# 401: the client retries exactly once per request, then returns
# whatever the server sends back. It does not retry forever.
client.close()
