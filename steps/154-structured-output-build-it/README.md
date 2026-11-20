# 154 - Structured Output: Hands On

Extends `AnthropicClient` with `generate_structured()` for forced tool-use JSON output, and adds `LLMTimeoutError` to `exceptions.py` so a timeout can be told apart from a generic API failure.

## Files (cumulative state of the shared `research_assistant` package as of this lesson)

```
src/research_assistant/__init__.py
src/research_assistant/exceptions.py
src/research_assistant/llm/__init__.py
src/research_assistant/llm/clients.py
```
