"""LLM provider clients, unified behind one interface.

BaseLLMClient defines the interface every provider client follows.
AnthropicClient and OpenAIClient each implement it for a real cloud
provider: this is the inheritance hierarchy the rest of the course
(and the capstone app in Course 4) builds on.

``BaseLLMClient``, ``AnthropicClient``, and ``OpenAIClient`` below, up to
the divider, are Course 2's (advanced-python-for-ai-engineers), copied
verbatim from
``steps/106-magic-methods-review/src/research_assistant/llm/clients.py``
once that course finished -- this file is owned by Course 2 per the
shared repo spec, and app/ only consumes it. One line was corrected on
copy: Course 2's shipped file has ``from .exceptions import ...``, which
looks for a nonexistent ``research_assistant.llm.exceptions`` module
(``clients.py`` lives inside the ``llm/`` package, so a single dot stays
inside it); this copy uses ``from ..exceptions import ...`` instead, so
the module actually imports. Flagged for Course 2 to fix in their own
steps/.

``AnthropicClient.generate_structured`` below the divider is a Course 4
addition: the Capstone needs Anthropic tool-use with a forced
``tool_choice`` for its cited-JSON answers (see rag/generator.py), which
``complete()`` has no way to express (it returns a plain string). Extending
the existing class with one more method -- rather than writing a second,
parallel Anthropic wrapper -- is exactly the pattern the LLM API Basics
lesson teaches for this situation. If Course 2 adds structured-output
support of its own later, reconcile the two rather than keeping both.
"""

from abc import ABC, abstractmethod
from typing import Any

import anthropic
import openai

from ..exceptions import LLMAPIError, LLMTimeoutError, RateLimitError


class BaseLLMClient(ABC):
    """Interface every LLM provider client must implement."""

    @abstractmethod
    def complete(self, prompt: str, **kwargs: Any) -> str:
        """Send prompt to the provider and return the text completion."""
        raise NotImplementedError


class AnthropicClient(BaseLLMClient):
    """Wraps anthropic.Anthropic() for text generation."""

    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514") -> None:
        self._client = anthropic.Anthropic(api_key=api_key)
        self.model = model

    def complete(self, prompt: str, max_tokens: int = 1024, **kwargs: Any) -> str:
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

    # --- Course 4 addition: see module docstring ---

    def generate_structured(
        self,
        messages: list[dict[str, str]],
        tool_name: str,
        tool_schema: dict[str, Any],
        tool_description: str = "",
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> dict[str, Any]:
        """Force a schema-conforming JSON reply via Anthropic tool use.

        Args:
            messages: Conversation to send.
            tool_name: Name of the single tool offered.
            tool_schema: JSON Schema describing the desired output shape.
            tool_description: Description shown to the model for the tool.
            system: Optional system prompt.
            max_tokens: Maximum output tokens.

        Returns:
            The tool's ``input`` dict, matching ``tool_schema``.

        Raises:
            LLMTimeoutError: The request timed out.
            RateLimitError: The provider rate-limited the request.
            LLMAPIError: Any other API failure, or a response with no
                tool_use block (the model did not use the tool).
        """
        kwargs: dict[str, Any] = dict(
            model=self.model,
            max_tokens=max_tokens,
            messages=messages,
            tools=[
                {
                    "name": tool_name,
                    "description": tool_description or f"Return {tool_name}",
                    "input_schema": tool_schema,
                }
            ],
            tool_choice={"type": "tool", "name": tool_name},
        )
        if system:
            kwargs["system"] = system

        try:
            response = self._client.messages.create(**kwargs)
        except anthropic.APITimeoutError as exc:
            raise LLMTimeoutError(provider="anthropic") from exc
        except anthropic.RateLimitError as exc:
            raise RateLimitError(provider="anthropic") from exc
        except anthropic.APIError as exc:
            raise LLMAPIError(str(exc), provider="anthropic") from exc

        for block in response.content:
            if block.type == "tool_use":
                return dict(block.input)
        raise LLMAPIError("Anthropic response contained no tool_use block", provider="anthropic")


class OpenAIClient(BaseLLMClient):
    """Wraps openai.OpenAI(). Used for text-embedding-3-small embeddings,
    but still implements complete() so it can stand in for any
    BaseLLMClient wherever one is expected."""

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4o-mini",
        embedding_model: str = "text-embedding-3-small",
    ) -> None:
        self._client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.embedding_model = embedding_model

    def complete(self, prompt: str, **kwargs: Any) -> str:
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
