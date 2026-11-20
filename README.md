# Doc Scout

Doc Scout is an AI research assistant API: a FastAPI service that ingests a
collection of text documents, answers questions about them with
retrieval-augmented generation (RAG), and returns a grounded answer with
citations instead of a guess. Ask it something it has no document for and
it says so, instead of making something up.

It chunks and embeds documents with OpenAI's `text-embedding-3-small`,
stores the vectors in a local Chroma collection, retrieves the most
relevant passages by cosine similarity, and asks Anthropic's Claude to
answer using only those passages, with its citations forced into a fixed
JSON shape via tool use. Repeat questions are served from a disk-persistent
cache instead of calling the model again. Everything sits behind a single
bearer token.

It is the companion code for the capstone of the Sypher course "AI
Development and Production Python": the fourth and final course in a
four-course track (`python-for-ai-engineers` ->
`advanced-python-for-ai-engineers` -> `data-and-apis-for-ai-engineers` ->
`ai-development-and-production-python`). `app/` is the finished project.

## What it needs that earlier courses didn't

This is the only course in the track that calls real, paid LLM APIs. You
need an Anthropic API key and an OpenAI API key (both are cloud accounts
with a card on file; `text-embedding-3-small` and Claude Sonnet calls for
working through this capstone cost a small amount, typically well under a
dollar). Nothing earlier in the track needs either key: you can clone this
repository as soon as you reach the earlier courses' Setup lesson, but you
will not need real keys until you start this course.

- Anthropic: https://console.anthropic.com/settings/keys
- OpenAI: https://platform.openai.com/api-keys

## Set up your computer

You need Git, Python 3.11 or newer, and Docker (Docker is only required
from the Docker lesson onward).

| Tool | Windows | macOS | Ubuntu or Debian |
| --- | --- | --- | --- |
| Git | `winget install --id Git.Git -e` | `brew install git` | `sudo apt update && sudo apt install -y git` |
| Python | `winget install Python.Python.3.12` | `brew install python@3.12` | `sudo apt install -y python3 python3-venv` |
| Docker | `winget install Docker.DockerDesktop`, then start Docker Desktop | `brew install --cask docker`, then start Docker Desktop | `curl -fsSL https://get.docker.com \| sh`, then `sudo usermod -aG docker $USER` and log back in |

Open a new terminal and check each tool:

```bash
git --version
python3 --version    # python --version on Windows
docker version       # needs a Server: section; start Docker Desktop if missing
```

### Get the code

```bash
git clone <doc-scout repository URL> doc-scout
cd doc-scout/app
```

Every command below runs from `app/`, the project root the service actually
builds from.

## Run the app

1. **Create and activate a virtual environment**, then install the package
   with its dev extras in editable mode:

   ```bash
   python3 -m venv .venv            # Windows: python -m venv .venv
   source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -e ".[dev]"
   ```

2. **Add your API keys.** Copy the example env file and fill in both keys
   plus a bearer token of your choosing (any long random string: the
   service only compares it, it never looks it up anywhere):

   ```bash
   cp .env.example .env
   ```

   ```bash
   # .env
   ANTHROPIC_API_KEY=sk-ant-...
   OPENAI_API_KEY=sk-...
   AUTH_TOKEN=pick-any-long-random-string
   ```

3. **Start the dev server:**

   ```bash
   python scripts/run.py
   ```

   or directly with Uvicorn:

   ```bash
   uvicorn research_assistant.main:app --reload
   ```

4. **Check it is alive** (no token needed: `/health` is always public):

   ```bash
   curl http://localhost:8000/health
   # {"status": "ok"}
   ```

5. **Ingest a document and ask about it:**

   ```bash
   curl -X POST http://localhost:8000/ingest \
     -H "Authorization: Bearer pick-any-long-random-string" \
     -H "Content-Type: application/json" \
     -d '{"doc_id": "python_intro", "text": "Python was created by Guido van Rossum and first released in 1991.", "source": "wikipedia"}'
   # {"doc_id": "python_intro", "chunk_count": 1}

   curl -X POST http://localhost:8000/ask \
     -H "Authorization: Bearer pick-any-long-random-string" \
     -H "Content-Type: application/json" \
     -d '{"question": "Who created Python and when?"}'
   # {"answer": "Python was created by Guido van Rossum...", "citations": [...], "latency_ms": 2140}
   ```

   Ask the same question again and it returns in a few milliseconds, with
   an `X-Cache-Hit: true` response header, instead of calling Claude again.

## Run it in Docker

```bash
docker build -t research-assistant .
docker run -p 8000:8000 --env-file .env research-assistant
```

Or, to persist the Chroma store, the cache, and the logs across restarts:

```bash
docker compose up --build
```

## Run the tests

```bash
pytest
```

Every test mocks the Anthropic and OpenAI boundary (the `llm/clients.py`
classes), so the suite needs no real API keys and makes no network calls,
including in CI. Tests that touch retrieval run against a real, temporary
Chroma store rather than mocking Chroma itself, so the actual similarity
search is exercised, not just the plumbing around it.

```bash
pytest --cov-fail-under=80
```

matches the coverage gate the GitHub Actions workflow enforces.

## Project layout

```text
doc-scout/
  app/
    src/research_assistant/
      config.py            Settings: API keys, Chroma path, chunking, cache TTL, model names
      exceptions.py         ResearchAssistantError and its subclasses
      logging_config.py     console (INFO) + rotating file (DEBUG) logging
      cache.py               disk-persistent QueryCache, keyed by SHA256(question)
      auth.py                 bearer-token FastAPI dependency
      models.py              Citation, AnswerResponse, request/response schemas
      llm/clients.py         AnthropicClient, OpenAIClient: retries, structured output, embeddings
      ingestion/
        chunker.py           chunk_text(): token-aligned chunks with overlap
        pipeline.py          IngestionPipeline: chunk -> embed -> store in Chroma
      rag/
        retriever.py         Retriever: embed query -> top-K Chroma cosine search
        generator.py         Generator: retrieved chunks -> cited answer via Claude tool use
        pipeline.py          RAGPipeline: cache check -> retrieve -> generate -> cache store
      main.py                 FastAPI app: routes, auth wiring, structured error handlers
    tests/                   pytest: one file per module above, plus test_main.py (API-level)
    configs/default.yaml     chunk size/overlap, top-K, cache TTL, model names, port
    scripts/run.py           starts the Uvicorn dev server
    Dockerfile                multi-stage, non-root user, HEALTHCHECK
    docker-compose.yml       app service with volumes for rag_db/, cache/, logs/
    pyproject.toml            dependencies, dev extras, ruff/mypy/pytest config
    .env.example              ANTHROPIC_API_KEY, OPENAI_API_KEY, AUTH_TOKEN
  steps/                     the project at the end of each lesson across all four courses
  .github/workflows/ci.yml   lint -> type-check -> test (coverage gate) -> Docker build/push
```

## Troubleshooting

- **`401 Unauthorized` on `/ask` or `/ingest`.** You forgot the
  `Authorization: Bearer <token>` header, or it doesn't match `AUTH_TOKEN`
  in `.env`. `/health` never needs it.
- **`500` with `cache_error` or `ingestion_error`.** Usually a bad or
  missing `CHROMA_PATH` / `CACHE_DIR`: both default to relative paths
  (`./rag_db`, `./cache`) resolved from wherever you launched the process.
  Run commands from `app/`, or set both to absolute paths in `.env`.
- **`408` on `/ask`.** The Anthropic or OpenAI call timed out. Check your
  network and that the key in `.env` is a real, active key, not the
  placeholder from `.env.example`.
- **`pytest` fails importing `research_assistant`.** You have not run
  `pip install -e ".[dev]"` yet, or you are running `pytest` from outside
  `app/`.
- **`docker build` is slow or the image is large.** The multi-stage
  Dockerfile only ships the installed Python packages and your code, not
  build tools; a first build still has to download and compile every
  dependency once, so expect a few minutes on a cold Docker cache.

## License

Copyright (C) 2026 SypherNext

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). You may
use, study and change it. If you share a modified version, or run one as a website or service
that other people use, you must make your full modified source code available under the same
license. See [LICENSE](LICENSE) for the full terms.
