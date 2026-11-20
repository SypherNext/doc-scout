import os
from http_client import HTTPClient

API_KEY = os.environ.get("OPENAI_API_KEY", "test-key")

# The client now accepts api_key: it attaches "Authorization: Bearer <key>"
# to the session headers once, instead of a separate auth client class.
client = HTTPClient(base_url="https://httpbin.org", api_key=API_KEY)

# httpbin echoes back the headers it received, so you can confirm it worked
response = client.get("/headers")
print(response.json()["headers"]["Authorization"])  # Bearer test-key
client.close()
