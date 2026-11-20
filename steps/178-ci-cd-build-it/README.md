# 178 - CI/CD: Hands On

Introduces the repo-root `.github/workflows/ci.yml` pipeline (lint -> type-check -> test -> Docker build/push). Not shown in this step's `src/` snapshot since it lives at the repo root, not under `app/`.

## Files (cumulative state of the shared `research_assistant` package as of this lesson)

```
.dockerignore
Dockerfile
docker-compose.yml
src/research_assistant/__init__.py
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
