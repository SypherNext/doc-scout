# 162 - RAG: Hands On

Introduces the real ingestion and RAG modules: `ingestion/chunker.py`, `ingestion/pipeline.py`, `rag/retriever.py`, `rag/generator.py`, `rag/pipeline.py`, and the `Citation`/`AnswerResponse` models they share. This is the thread that survives into Docker/CI-CD and the Capstone.

## Files (cumulative state of the shared `research_assistant` package as of this lesson)

```
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
```
