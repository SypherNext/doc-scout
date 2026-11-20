"""Tests for research_assistant.llm.clients.

AnthropicClient and OpenAIClient are Course 2's (copied verbatim once that
course finished; see the module docstring in llm/clients.py). These tests
patch the underlying SDK objects (``_client``) directly, rather than
mocking the wrapper classes themselves, so the error mapping and the
Course 4 addition (``generate_structured``) are the things actually under
test.
"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

import anthropic
import openai
import pytest

from research_assistant.exceptions import LLMAPIError, LLMTimeoutError, RateLimitError
from research_assistant.llm.clients import AnthropicClient, OpenAIClient


@pytest.fixture
def anthropic_client() -> AnthropicClient:
    client = AnthropicClient(api_key="test-key")
    client._client = MagicMock()
    return client


@pytest.fixture
def openai_client() -> OpenAIClient:
    client = OpenAIClient(api_key="test-key")
    client._client = MagicMock()
    return client


def _fake_request_error(exc_cls):
    """Build a real anthropic/openai SDK error that only takes a `request`."""
    return exc_cls(request=MagicMock())


def _fake_status_error(exc_cls, status_code, message="boom"):
    response = MagicMock(status_code=status_code)
    return exc_cls(message=message, response=response, body=None)


def test_anthropic_complete_returns_text(anthropic_client: AnthropicClient) -> None:
    anthropic_client._client.messages.create.return_value = SimpleNamespace(
        content=[SimpleNamespace(type="text", text="hi there")]
    )

    result = anthropic_client.complete("hi")

    assert result == "hi there"


def test_anthropic_complete_wraps_rate_limit_error(anthropic_client: AnthropicClient) -> None:
    anthropic_client._client.messages.create.side_effect = _fake_status_error(
        anthropic.RateLimitError, status_code=429
    )

    with pytest.raises(RateLimitError):
        anthropic_client.complete("hi")


def test_anthropic_complete_wraps_generic_api_error(anthropic_client: AnthropicClient) -> None:
    anthropic_client._client.messages.create.side_effect = _fake_status_error(
        anthropic.APIStatusError, status_code=500
    )

    with pytest.raises(LLMAPIError):
        anthropic_client.complete("hi")


def test_generate_structured_returns_tool_input(anthropic_client: AnthropicClient) -> None:
    anthropic_client._client.messages.create.return_value = SimpleNamespace(
        content=[
            SimpleNamespace(type="text", text="thinking..."),
            SimpleNamespace(type="tool_use", input={"answer": "42", "citations": []}),
        ]
    )

    result = anthropic_client.generate_structured(
        messages=[{"role": "user", "content": "q"}],
        tool_name="answer_question",
        tool_schema={"type": "object", "properties": {}},
    )

    assert result == {"answer": "42", "citations": []}


def test_generate_structured_raises_when_no_tool_use_block(
    anthropic_client: AnthropicClient,
) -> None:
    anthropic_client._client.messages.create.return_value = SimpleNamespace(
        content=[SimpleNamespace(type="text", text="no tool here")]
    )

    with pytest.raises(LLMAPIError):
        anthropic_client.generate_structured(
            messages=[{"role": "user", "content": "q"}],
            tool_name="answer_question",
            tool_schema={"type": "object", "properties": {}},
        )


def test_generate_structured_raises_llm_timeout_on_sdk_timeout(
    anthropic_client: AnthropicClient,
) -> None:
    anthropic_client._client.messages.create.side_effect = _fake_request_error(
        anthropic.APITimeoutError
    )

    with pytest.raises(LLMTimeoutError):
        anthropic_client.generate_structured(
            messages=[{"role": "user", "content": "q"}],
            tool_name="answer_question",
            tool_schema={"type": "object", "properties": {}},
        )


def test_generate_structured_raises_rate_limit_on_429(anthropic_client: AnthropicClient) -> None:
    anthropic_client._client.messages.create.side_effect = _fake_status_error(
        anthropic.RateLimitError, status_code=429
    )

    with pytest.raises(RateLimitError):
        anthropic_client.generate_structured(
            messages=[{"role": "user", "content": "q"}],
            tool_name="answer_question",
            tool_schema={"type": "object", "properties": {}},
        )


def test_openai_complete_returns_text(openai_client: OpenAIClient) -> None:
    openai_client._client.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content="hi"))]
    )

    assert openai_client.complete("hi") == "hi"


def test_openai_complete_wraps_rate_limit_error(openai_client: OpenAIClient) -> None:
    openai_client._client.chat.completions.create.side_effect = _fake_status_error(
        openai.RateLimitError, status_code=429
    )

    with pytest.raises(RateLimitError):
        openai_client.complete("hi")


def test_openai_embed_returns_a_single_vector(openai_client: OpenAIClient) -> None:
    openai_client._client.embeddings.create.return_value = SimpleNamespace(
        data=[SimpleNamespace(embedding=[0.1, 0.2, 0.3])]
    )

    vector = openai_client.embed("some text")

    assert vector == [0.1, 0.2, 0.3]
    openai_client._client.embeddings.create.assert_called_once_with(
        model="text-embedding-3-small", input="some text"
    )


def test_openai_embed_wraps_api_error(openai_client: OpenAIClient) -> None:
    openai_client._client.embeddings.create.side_effect = _fake_status_error(
        openai.APIStatusError, status_code=500
    )

    with pytest.raises(LLMAPIError):
        openai_client.embed("some text")
