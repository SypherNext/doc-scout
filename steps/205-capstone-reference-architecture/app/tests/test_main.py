"""Integration tests for the FastAPI app, hitting routes through TestClient.

The LLM/embedding clients are real objects (constructing them makes no
network call), but the pipelines they would be used by are swapped for
mocks after startup, so no test here ever reaches a real external API.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from research_assistant.config import load_config
from research_assistant.models import AnswerResponse


@pytest.fixture
def client(monkeypatch, tmp_path):
    monkeypatch.setenv("AUTH_TOKEN", "test-token")
    # Non-empty placeholders: constructing the SDK clients only validates
    # that *some* key string was given, it never makes a network call.
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-anthropic-key")
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    # Point every on-disk store at a temp dir: the app's lifespan opens a
    # real Chroma client, cache, and log file on startup, and the defaults
    # (./rag_db, ./cache, ./logs) would otherwise write into the project
    # directory itself whenever this test runs.
    monkeypatch.setenv("CHROMA_PATH", str(tmp_path / "rag_db"))
    monkeypatch.setenv("CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("LOG_DIR", str(tmp_path / "logs"))
    load_config.cache_clear()

    from research_assistant.main import app

    with TestClient(app) as test_client:
        app.state.ingestion_pipeline = MagicMock()
        app.state.ingestion_pipeline.ingest_document.return_value = 3

        app.state.rag_pipeline = MagicMock()
        app.state.rag_pipeline.answer.return_value = MagicMock(
            response=AnswerResponse(answer="Test answer.", citations=[], latency_ms=10),
            cache_hit=False,
        )
        yield test_client

    load_config.cache_clear()


def test_health_is_always_public(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_without_auth_header_returns_401(client: TestClient) -> None:
    response = client.post("/ask", json={"question": "What is Python?"})
    assert response.status_code == 401
    assert response.json()["error"] == "auth_error"


def test_ask_with_wrong_token_returns_403(client: TestClient) -> None:
    response = client.post(
        "/ask",
        json={"question": "What is Python?"},
        headers={"Authorization": "Bearer wrong-token"},
    )
    assert response.status_code == 403


def test_ask_with_valid_token_returns_200(client: TestClient) -> None:
    response = client.post(
        "/ask",
        json={"question": "What is Python?"},
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["answer"] == "Test answer."
    assert response.headers["X-Cache-Hit"] == "false"


def test_ask_with_empty_question_returns_422(client: TestClient) -> None:
    response = client.post(
        "/ask",
        json={"question": ""},
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 422
    assert response.json()["error"] == "validation_error"


def test_ingest_without_auth_returns_401(client: TestClient) -> None:
    response = client.post("/ingest", json={"doc_id": "d1", "text": "hello"})
    assert response.status_code == 401


def test_ingest_with_valid_token_returns_chunk_count(client: TestClient) -> None:
    response = client.post(
        "/ingest",
        json={"doc_id": "d1", "text": "hello world"},
        headers={"Authorization": "Bearer test-token"},
    )
    assert response.status_code == 200
    assert response.json() == {"doc_id": "d1", "chunk_count": 3}
