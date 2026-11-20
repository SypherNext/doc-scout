# 106 - Magic Methods: Review

Upgrades models.py: Citation and AnswerResponse get custom __repr__ (truncated, readable) and __eq__ (equality that excludes fields which legitimately vary between runs: relevance_score ordering jitter and latency_ms).

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
