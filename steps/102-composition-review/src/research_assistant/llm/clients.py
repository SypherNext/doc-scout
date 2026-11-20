"""LLM provider clients, unified behind one interface.

BaseLLMClient defines the interface every provider client follows.
AnthropicClient and OpenAIClient each implement it for a real cloud
provider: this is the inheritance hierarchy the rest of the course
(and the capstone app in Course 4) builds on.
"""
from abc import ABC, abstractmethod

import anthropic
import openai

from ..exceptions import LLMAPIError, RateLimitError


class BaseLLMClient(ABC):
    """Interface every LLM provider client must implement."""

    @abstractmethod
    def complete(self, prompt: str, **kwargs) -> str:
        """Send prompt to the provider and return the text completion."""
        raise NotImplementedError


class AnthropicClient(BaseLLMClient):
    """Wraps anthropic.Anthropic() for text generation."""

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self._client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def complete(self, prompt: str, max_tokens: int = 1024, **kwargs) -> str:
        try:
            response = self._client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
        except anthropic.RateLimitError as exc:
            raise RateLimitError(provider="anthropic") from exc
        except anthropic.APIError as exc:
            raise LLMAPIError(str(exc), provider="anthropic") from exc
        return response.content[0].text


class OpenAIClient(BaseLLMClient):
    """Wraps openai.OpenAI(). Used for text-embedding-3-small embeddings,
    but still implements complete() so it can stand in for any
    BaseLLMClient wherever one is expected."""

    def __init__(self, api_key: str, model: str = "gpt-4o-mini", embedding_model: str = "text-embedding-3-small"):
        self._client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.embedding_model = embedding_model

    def complete(self, prompt: str, **kwargs) -> str:
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
        except openai.RateLimitError as exc:
            raise RateLimitError(provider="openai") from exc
        except openai.APIError as exc:
            raise LLMAPIError(str(exc), provider="openai") from exc
        return response.choices[0].message.content

    def embed(self, text: str) -> list[float]:
        """Provider-specific extension: not part of BaseLLMClient, because
        not every provider offers embeddings the same way."""
        try:
            response = self._client.embeddings.create(
                model=self.embedding_model,
                input=text,
            )
        except openai.RateLimitError as exc:
            raise RateLimitError(provider="openai") from exc
        except openai.APIError as exc:
            raise LLMAPIError(str(exc), provider="openai") from exc
        return response.data[0].embedding
