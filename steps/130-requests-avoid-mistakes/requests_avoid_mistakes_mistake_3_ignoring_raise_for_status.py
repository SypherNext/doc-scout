import requests

response = requests.get("https://httpbin.org/status/404")
# No error raised: response.status_code is 404, but the code continues
data = response.json()  # May fail or return unexpected content


response = requests.get(url, timeout=10)
response.raise_for_status()  # Raises HTTPError for 4xx/5xx
data = response.json()
