# 096 - Inheritance: Hands On

Upgrades llm/clients.py: introduces BaseLLMClient(ABC) with an abstract complete() method; AnthropicClient now inherits from it, and OpenAIClient joins as a second implementation (plus its own embed() method for text-embedding-3-small).

## Files

```
src/research_assistant/
  __init__.py
  cache.py
  decorators.py
  exceptions.py
  llm/__init__.py
  llm/clients.py
  logging_config.py
  models.py
```
