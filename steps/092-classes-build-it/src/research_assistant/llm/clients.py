"""A first LLM client, written as a plain concrete class.

This version has no abstract base class and no second provider: it
exists to practice class mechanics (attributes, methods, properties,
classmethods, staticmethods) on code that will later be factored into
an inheritance hierarchy (Inheritance lesson) when OpenAIClient joins
it.
"""
import os

import anthropic


class AnthropicClient:
    """Wraps anthropic.Anthropic() to send a prompt and get text back."""

    SUPPORTED_MODELS = {
        "claude-sonnet-4-20250514",
        "claude-opus-4-20250514",
    }

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self._client = anthropic.Anthropic(api_key=api_key)
        self._model = model
        self.call_count = 0

    @property
    def model(self) -> str:
        """Getter for the configured model name."""
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        """Setter with validation: only known model names are allowed."""
        if not self.is_supported_model(value):
            raise ValueError(f"Unsupported model: {value}")
        self._model = value

    def complete(self, prompt: str, max_tokens: int = 1024) -> str:
        """Send prompt to Claude and return the text completion."""
        self.call_count += 1
        response = self._client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

    @classmethod
    def from_env(cls) -> "AnthropicClient":
        """Alternative constructor: read the API key from the environment."""
        api_key = os.environ["ANTHROPIC_API_KEY"]
        return cls(api_key)

    @staticmethod
    def is_supported_model(model: str) -> bool:
        """Utility check that does not need an instance."""
        return model in AnthropicClient.SUPPORTED_MODELS

    def __str__(self) -> str:
        return f"AnthropicClient(model={self._model}, calls={self.call_count})"
