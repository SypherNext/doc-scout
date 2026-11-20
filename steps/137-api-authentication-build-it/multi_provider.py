import os
from http_client import HTTPClient

PROVIDERS = {
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "env_var": "OPENAI_API_KEY",
    },
    "anthropic": {
        "base_url": "https://api.anthropic.com/v1",
        "env_var": "ANTHROPIC_API_KEY",
        "extra_headers": {"anthropic-version": "2023-06-01"},
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "env_var": "GROQ_API_KEY",
    },
}

class MultiProviderClients:
    """Builds and caches one HTTPClient per configured provider."""

    def __init__(self):
        self._clients: dict[str, HTTPClient] = {}

    def get(self, provider: str) -> HTTPClient:
        if provider not in self._clients:
            config = PROVIDERS.get(provider)
            if not config:
                raise ValueError(f"Unknown provider: {provider}")

            api_key = os.environ.get(config["env_var"])
            if not api_key:
                raise ValueError(f"Set {config['env_var']} environment variable")

            self._clients[provider] = HTTPClient(
                base_url=config["base_url"],
                api_key=api_key,
                headers=config.get("extra_headers"),
            )
        return self._clients[provider]

    def close(self):
        for client in self._clients.values():
            client.close()

# Usage
clients = MultiProviderClients()

try:
    configured = [p for p in PROVIDERS if os.environ.get(PROVIDERS[p]["env_var"])]
    if configured:
        print(f"Configured providers: {', '.join(configured)}")
    else:
        print("No provider API keys found. Set OPENAI_API_KEY, ANTHROPIC_API_KEY, etc.")
except Exception as e:
    print(f"Error: {e}")
finally:
    clients.close()
