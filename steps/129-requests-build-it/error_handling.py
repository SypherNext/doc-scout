import requests

# Simulate various HTTP responses
urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
]

for url in urls:
    response = requests.get(url)
    print(f"{url}: {response.status_code}", end=" ")

    if response.ok:  # True for 200-399
        print("OK")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code >= 500:
        print("Server error")

# raise_for_status(): raise an exception for error codes
try:
    response = requests.get("https://httpbin.org/status/404")
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")

# Connection error (no network or wrong domain)
try:
    requests.get("https://nonexistent-domain-xyz.com", timeout=5)
except requests.exceptions.ConnectionError as e:
    print(f"Connection error: {e}")

# Timeout
try:
    requests.get("https://httpbin.org/delay/10", timeout=3)
except requests.exceptions.Timeout as e:
    print(f"Timeout: {e}")
