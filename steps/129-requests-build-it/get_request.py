import requests

response = requests.get("https://httpbin.org/json")
print(response.status_code)          # 200
print(response.headers["content-type"])  # application/json

# Parse JSON response
data = response.json()
print(data["slideshow"]["title"])    # Sample Slide Show

# Text response (for non-JSON)
# print(response.text)
