"""Exception hierarchy for the Doc Scout research assistant.

Every error raised by research_assistant code inherits from
ResearchAssistantError, so calling code can do:

    try:
        ...
    except ResearchAssistantError as exc:
        ...

and catch anything the package raises, or catch one of the specific
subclasses below when it needs to react differently to different
failures.

This file's base classes (``ResearchAssistantError``, ``LLMAPIError``,
``RateLimitError``, ``IngestionError``, ``AuthError``, ``CacheError``) are
Course 2's (advanced-python-for-ai-engineers), copied verbatim from
``steps/106-magic-methods-review/src/research_assistant/exceptions.py`` once
that course finished -- this file is owned by Course 2 per the shared repo
spec, and app/ only consumes it.

``LLMTimeoutError``, ``MissingTokenError``, and ``InvalidTokenError`` below
the divider are Course 4 additions: the Capstone's own error-handling
requirements need a timeout distinct from a generic LLM API failure (so
``/ask`` can return 408, not just 502) and two distinct auth failures (401
for no token, 403 for a wrong one), and neither exists in Course 2's
canonical file. If Course 2 adds its own timeout/auth subclasses later,
reconcile these with theirs rather than keeping two definitions.
"""


class ResearchAssistantError(Exception):
    """Base class for every error raised by research_assistant."""


class LLMAPIError(ResearchAssistantError):
    """Raised when a call to an LLM provider (Anthropic or OpenAI) fails."""

    def __init__(
        self, message: str, provider: str | None = None, status_code: int | None = None
    ) -> None:
        self.provider = provider
        self.status_code = status_code
        super().__init__(message)


class RateLimitError(LLMAPIError):
    """Raised when a provider responds with a rate-limit error (HTTP 429).

    This is the ONE definition of RateLimitError in the project. It is a
    kind of LLMAPIError (rate limiting is a specific flavor of "the LLM
    API call failed"), so any code that catches LLMAPIError also catches
    RateLimitError.
    """

    def __init__(self, provider: str | None = None, retry_after: float | None = None) -> None:
        self.retry_after = retry_after
        message = f"Rate limited by {provider}" if provider else "Rate limited"
        if retry_after is not None:
            message += f", retry after {retry_after}s"
        super().__init__(message, provider=provider, status_code=429)


class IngestionError(ResearchAssistantError):
    """Raised when loading or chunking a document collection fails."""


class AuthError(ResearchAssistantError):
    """Raised when a request's bearer token is missing or invalid."""


class CacheError(ResearchAssistantError):
    """Raised when the query cache cannot be read from or written to."""


# --- Course 4 (Capstone) additions below: see module docstring ---


class LLMTimeoutError(LLMAPIError):
    """Raised when a call to an LLM or embedding provider times out.

    A kind of LLMAPIError, same as RateLimitError, so existing
    ``except LLMAPIError`` handlers keep working; the Capstone's own
    `/ask` route distinguishes this one to return 408 instead of 502.
    """

    def __init__(self, provider: str | None = None) -> None:
        message = f"Timed out waiting for {provider}" if provider else "Request timed out"
        super().__init__(message, provider=provider, status_code=408)


class MissingTokenError(AuthError):
    """No ``Authorization`` header was supplied. Maps to HTTP 401."""


class InvalidTokenError(AuthError):
    """A bearer token was supplied but does not match ``AUTH_TOKEN``. Maps to HTTP 403."""
