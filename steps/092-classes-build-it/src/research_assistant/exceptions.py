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
"""


class ResearchAssistantError(Exception):
    """Base class for every error raised by research_assistant."""


class LLMAPIError(ResearchAssistantError):
    """Raised when a call to an LLM provider (Anthropic or OpenAI) fails."""

    def __init__(self, message: str, provider: str | None = None, status_code: int | None = None):
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

    def __init__(self, provider: str | None = None, retry_after: float | None = None):
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
