# 076 - Error Handling: Hands On

Adds exceptions.py: ResearchAssistantError and its subclasses (LLMAPIError, RateLimitError(LLMAPIError), IngestionError, AuthError, CacheError) -- ONE definition each, used everywhere from here on. decorators.py and cache.py are upgraded to use them (retry_with_backoff now catches LLMAPIError; QueryCache wraps failures in CacheError).

## Files

```
src/research_assistant/
  __init__.py
  cache.py
  decorators.py
  exceptions.py
```
