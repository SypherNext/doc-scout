# 186 - Project Structure: Hands On

Introduces `configs/default.yaml`, `config.py` (pydantic Settings), and `scripts/run.py`: the project's configuration and entry point.

## Files (cumulative state of the shared `research_assistant` package as of this lesson)

```
.dockerignore
Dockerfile
configs/default.yaml
docker-compose.yml
pyproject.toml
scripts/run.py
src/research_assistant/__init__.py
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
