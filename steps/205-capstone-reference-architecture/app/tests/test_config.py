"""Tests for research_assistant.config.load_config.

The regression this guards against: pydantic-settings gives constructor
keyword arguments higher priority than environment variables, so naively
passing every YAML default straight through as a kwarg would silently
defeat "environment variables always win" for every YAML-backed field.
"""

from __future__ import annotations

from research_assistant.config import load_config


def test_env_var_overrides_yaml_default(monkeypatch, tmp_path):
    monkeypatch.setenv("CHROMA_PATH", str(tmp_path / "custom_rag_db"))
    load_config.cache_clear()

    settings = load_config()

    assert settings.chroma_path == str(tmp_path / "custom_rag_db")
    load_config.cache_clear()


def test_yaml_default_applies_when_no_env_var_is_set(monkeypatch):
    monkeypatch.delenv("CHROMA_PATH", raising=False)
    load_config.cache_clear()

    settings = load_config()

    # configs/default.yaml ships "./rag_db"; this is the actual file on
    # disk, not a mock, so this also catches the config file going missing
    # or being renamed.
    assert settings.chroma_path == "./rag_db"
    load_config.cache_clear()


def test_env_var_overrides_a_field_with_no_explicit_alias(monkeypatch, tmp_path):
    # collection_name has no `alias=` in Settings, so this also exercises
    # the plain-uppercase-fieldname branch of the override check.
    monkeypatch.setenv("COLLECTION_NAME", "overridden_docs")
    load_config.cache_clear()

    settings = load_config()

    assert settings.collection_name == "overridden_docs"
    load_config.cache_clear()


def test_secrets_are_empty_by_default_and_never_come_from_yaml(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("AUTH_TOKEN", raising=False)
    load_config.cache_clear()

    settings = load_config()

    assert settings.anthropic_api_key == ""
    assert settings.openai_api_key == ""
    assert settings.auth_token == ""
    load_config.cache_clear()
