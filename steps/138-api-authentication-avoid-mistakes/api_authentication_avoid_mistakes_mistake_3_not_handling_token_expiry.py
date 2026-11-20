import requests

def get_token():
    """Stand-in for a real call to your auth server's token endpoint."""
    return {"access_token": "sk-short-lived-token", "expires_in": 3600}

# Get a token that expires in 1 hour
token = get_token()  # {"access_token": "...", "expires_in": 3600}

# Use it an hour later: will fail with 401
headers = {"Authorization": f"Bearer {token['access_token']}"}
response = requests.get("https://api.example.com/data", headers=headers)
# 401 Unauthorized: token expired


import time

expires_at = time.time() + token["expires_in"] - 60  # 60s buffer
if time.time() >= expires_at:
    token = refresh_token()  # Get a new token
