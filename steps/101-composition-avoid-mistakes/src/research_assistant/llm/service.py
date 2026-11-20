"""LLMService: composition in action.

LLMService does not inherit from BaseLLMClient. It HAS one (injected
through the constructor), plus a QueryCache and the retry/logging
decorators applied to its own method. This is the "has-a" alternative
to the inheritance hierarchy in llm/clients.py: a service built by
combining a client, a cache, and cross-cutting behaviour.
"""
from ..cache import QueryCache
from ..decorators import log_calls, retry_with_backoff
from .clients import BaseLLMClient


class LLMService:
    """Composes an LLM client with a query cache and retry/logging."""

    def __init__(self, client: BaseLLMClient, cache: QueryCache):
        self.client = client
        self.cache = cache

    @log_calls
    @retry_with_backoff
    def ask(self, prompt: str, doc_ids: list[str]) -> str:
        """Answer prompt, using the cache when the same question has
        already been asked against the same documents."""
        cached = self.cache.get(prompt, doc_ids)
        if cached is not None:
            return cached

        result = self.client.complete(prompt)
        self.cache.set(prompt, doc_ids, result)
        return result
