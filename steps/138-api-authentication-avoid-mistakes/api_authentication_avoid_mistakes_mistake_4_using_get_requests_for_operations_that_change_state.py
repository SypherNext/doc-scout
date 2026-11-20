import requests

API_KEY = "sk-test-placeholder"

# WRONG, GET should be idempotent
response = requests.get(
    "https://api.example.com/models/gpt-4/delete",
    headers={"Authorization": f"Bearer {API_KEY}"},
)
