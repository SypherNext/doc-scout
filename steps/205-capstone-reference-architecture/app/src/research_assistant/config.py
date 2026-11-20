"""Application configuration.

Tunable values (chunk size, overlap, top-K, cache TTL, model names, port)
come from ``configs/default.yaml``. Secrets and any per-deployment override
come from environment variables (or a local ``.env`` file loaded by
``pydantic-settings``) and always win over the YAML file, so a secret never
has to be written to a file that could end up in the Docker image or the
repo.
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import Field
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings, SettingsConfigDict

# app/src/research_assistant/config.py -> app/configs/default.yaml
_APP_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = _APP_ROOT / "configs" / "default.yaml"


def _load_yaml_defaults(path: Path) -> dict[str, Any]:
    """Read the YAML config file, returning an empty dict if it is absent.

    A missing file is not an error: the pydantic field defaults below cover
    local development and tests that never ship a configs/ directory.
    """
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return data or {}


class Settings(BaseSettings):
    """Every tunable value the research assistant needs, in one place.

    Precedence (highest wins): process environment variables > ``.env`` file
    > ``configs/default.yaml`` > the field default below.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True,
        extra="ignore",
    )

    # --- Secrets: environment variables only, never logged or persisted ---
    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    auth_token: str = Field(default="", alias="AUTH_TOKEN")

    # --- Storage paths ---
    chroma_path: str = Field(default="./rag_db", alias="CHROMA_PATH")
    collection_name: str = "rag_docs"
    cache_dir: str = Field(default="./cache", alias="CACHE_DIR")
    log_dir: str = "./logs"

    # --- Caching ---
    cache_ttl_seconds: int = Field(default=3600, alias="CACHE_TTL_SECONDS")

    # --- Chunking (RAG lesson's chunk_text: 500 tokens, 100 overlap) ---
    chunk_size: int = 500
    chunk_overlap: int = 100

    # --- Retrieval ---
    top_k: int = 3

    # --- Models ---
    anthropic_model: str = "claude-sonnet-4-20250514"
    embedding_model: str = "text-embedding-3-small"

    # --- Web server ---
    port: int = 8000


def _has_env_override(field_name: str, field: FieldInfo) -> bool:
    """Check whether an environment variable already supplies ``field_name``.

    ``pydantic-settings`` gives constructor keyword arguments *higher*
    priority than environment variables. Passing every YAML value straight
    through as a keyword argument would therefore silently defeat "env
    vars always win": an env var like ``CHROMA_PATH`` set to point tests
    at a temp directory would be ignored in favour of the YAML file's
    ``./rag_db``. Checking for an override here, and omitting that key
    from the YAML dict entirely, lets ``Settings()`` fall through to its
    own (correct) environment-variable handling for that field instead.
    """
    candidates = {field_name, field_name.upper()}
    if field.alias:
        candidates.add(field.alias)
        candidates.add(field.alias.upper())
    return any(candidate in os.environ for candidate in candidates)


@lru_cache
def load_config() -> Settings:
    """Return the process-wide :class:`Settings`, built once and cached.

    Cached with ``lru_cache`` so every module that calls ``load_config()``
    shares one instance instead of re-reading the YAML file and re-parsing
    environment variables on every call. Tests that need a different
    configuration should construct ``Settings(...)`` directly instead of
    relying on this cache.
    """
    yaml_defaults = _load_yaml_defaults(DEFAULT_CONFIG_PATH)
    yaml_overrides = {
        key: value
        for key, value in yaml_defaults.items()
        if key in Settings.model_fields
        and not _has_env_override(key, Settings.model_fields[key])
    }
    return Settings(**yaml_overrides)
