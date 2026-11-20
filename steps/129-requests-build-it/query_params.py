import requests

# Pass query parameters as a dict
params = {
    "q": "AI engineering",
    "page": 1,
    "limit": 10,
}
response = requests.get("https://httpbin.org/get", params=params)

# Check the URL that was actually requested
print(response.url)
# https://httpbin.org/get?q=AI+engineering&page=1&limit=10

# The response echoes back what was sent
data = response.json()
print(data["args"]["q"])  # AI engineering
