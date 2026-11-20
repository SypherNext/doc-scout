import requests

# Without timeout: can hang forever
response = requests.get("https://api.example.com/slow-endpoint")

# With timeout: raises after 10 seconds
response = requests.get("https://api.example.com/slow-endpoint", timeout=10)


response = requests.get(url, timeout=(3.05, 10))  # 3s connect, 10s read
