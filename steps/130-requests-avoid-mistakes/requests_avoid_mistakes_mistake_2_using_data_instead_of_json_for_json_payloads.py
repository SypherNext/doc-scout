import requests

url = "https://httpbin.org/post"

# Wrong: sends form-encoded data, not JSON
response = requests.post(url, data={"model": "gpt-4"})
# Content-Type: application/x-www-form-urlencoded
# The server may not parse this correctly

# Correct: sends JSON
response = requests.post(url, json={"model": "gpt-4"})
# Content-Type: application/json
