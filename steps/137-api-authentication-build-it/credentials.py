import os
import json
from pathlib import Path

class CredentialManager:
    """Load credentials from environment variables or a secure file."""

    REQUIRED_KEYS = {
        "openai": ["api_key"],
        "anthropic": ["api_key"],
        "huggingface": ["api_token"],
    }

    def __init__(self, env_prefix: str = "AI_CREDS"):
        self.env_prefix = env_prefix

    def get(self, provider: str, key: str) -> str:
        """Get a credential from environment variables."""
        env_key = f"{self.env_prefix}_{provider.upper()}_{key.upper()}"
        value = os.environ.get(env_key)
        if not value:
            raise ValueError(
                f"Missing credential: set {env_key} environment variable"
            )
        return value

    def get_all(self, provider: str) -> dict:
        """Get all credentials for a provider."""
        creds = {}
        for key in self.REQUIRED_KEYS.get(provider, []):
            creds[key] = self.get(provider, key)
        return creds

# Usage
mgr = CredentialManager(env_prefix="AI_CREDS")

# Set before running:
# export AI_CREDS_OPENAI_API_KEY="sk-..."
# export AI_CREDS_ANTHROPIC_API_KEY="sk-ant-..."

try:
    openai_key = mgr.get("openai", "api_key")
    print(f"OpenAI key loaded: {openai_key[:8]}...")
except ValueError as e:
    print(f"Note: {e}")
