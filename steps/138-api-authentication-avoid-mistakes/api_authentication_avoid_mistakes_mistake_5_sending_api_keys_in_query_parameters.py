import requests

# WRONG: key in URL
response = requests.get(
    "https://api.example.com/data?api_key=sk-abc123..."
)

# The URL may be:
# 1. Logged by web servers and proxies
# 2. Visible in browser history
# 3. Sent in the Referer header to other sites
# 4. Cached by CDNs
