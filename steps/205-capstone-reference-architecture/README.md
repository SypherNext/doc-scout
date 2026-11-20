# 205 - Reference Architecture

No changes to the shared `research_assistant` package at this lesson. See the lesson text for its own standalone example code.

## Files (cumulative state of the shared `research_assistant` package as of this lesson)

```
.dockerignore
Dockerfile
configs/default.yaml
docker-compose.yml
pyproject.toml
scripts/run.py
src/research_assistant/__init__.py
src/research_assistant/auth.py
src/research_assistant/cache.py
src/research_assistant/config.py
src/research_assistant/exceptions.py
src/research_assistant/ingestion/__init__.py
src/research_assistant/ingestion/chunker.py
src/research_assistant/ingestion/pipeline.py
src/research_assistant/llm/__init__.py
src/research_assistant/llm/clients.py
src/research_assistant/models.py
src/research_assistant/rag/__init__.py
src/research_assistant/rag/generator.py
src/research_assistant/rag/pipeline.py
src/research_assistant/rag/retriever.py
tests/conftest.py
tests/test_cache.py
tests/test_chunker.py
tests/test_llm_clients.py
```

## Complete project

This step also includes a full copy of `app/` (the finished Doc Scout service) under `app/` in this folder, since this is the last lesson of the course and the Reference Architecture explicitly shows the finished shape of the project.
