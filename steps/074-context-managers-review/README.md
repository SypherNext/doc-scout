# 074 - Context Managers: Review

Adds cache.py: QueryCache (diskcache-backed, keyed by sha256 of query+doc_ids) and CacheContext, a class-based context manager that safely opens/closes it.

## Files

```
src/research_assistant/
  __init__.py
  cache.py
  decorators.py
```
