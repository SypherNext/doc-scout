import requests
from http_client import HTTPClient

def make_token_provider(client_id: str, client_secret: str, auth_url: str):
    """Build an OAuth2 client-credentials token provider.

    Returns a callable that HTTPClient calls whenever its cached token
    has expired. httpbin echoes the request back so you can see the
    exchange happen without a real auth server.
    """
    def fetch_token() -> tuple[str, int]:
        response = requests.post(
            auth_url,
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials",
            },
            timeout=10,
        )
        response.raise_for_status()
        # A real OAuth2 server would return {"access_token": "...", "expires_in": 3600}
        return "sk-refreshed-token", 3600  # token, expires_in seconds
    return fetch_token

client = HTTPClient(
    base_url="https://httpbin.org",
    token_provider=make_token_provider(
        client_id="your-client-id",
        client_secret="your-client-secret",
        auth_url="https://httpbin.org/post",
    ),
)

# The first request triggers a token fetch; the token is then cached
# until it is within 60 seconds of expiring.
response = client.get("/headers")
print(f"Auth header present: {'Authorization' in response.request.headers}")
client.close()
