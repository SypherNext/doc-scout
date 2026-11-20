# 101 - Composition: Common Mistakes

Adds llm/service.py: LLMService, which HAS a BaseLLMClient and a QueryCache (injected, not created internally) and applies @log_calls/@retry_with_backoff to its own ask() method. This is the has-a alternative to the clients.py inheritance hierarchy.

## Files

```
src/research_assistant/
  __init__.py
  cache.py
  decorators.py
  exceptions.py
  llm/__init__.py
  llm/clients.py
  llm/service.py
  logging_config.py
  models.py
```
