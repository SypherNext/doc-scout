"""Tests for research_assistant.auth.verify_bearer_token."""

from __future__ import annotations

import pytest

from research_assistant.auth import verify_bearer_token
from research_assistant.config import Settings
from research_assistant.exceptions import InvalidTokenError, MissingTokenError


def _settings(auth_token: str = "secret-token") -> Settings:
    return Settings(AUTH_TOKEN=auth_token)


def test_valid_token_is_accepted() -> None:
    token = verify_bearer_token(authorization="Bearer secret-token", settings=_settings())
    assert token == "secret-token"


def test_missing_authorization_header_raises_missing_token_error() -> None:
    with pytest.raises(MissingTokenError):
        verify_bearer_token(authorization=None, settings=_settings())


def test_header_without_bearer_prefix_raises_missing_token_error() -> None:
    with pytest.raises(MissingTokenError):
        verify_bearer_token(authorization="secret-token", settings=_settings())


def test_bearer_prefix_with_empty_token_raises_missing_token_error() -> None:
    with pytest.raises(MissingTokenError):
        verify_bearer_token(authorization="Bearer ", settings=_settings())


def test_wrong_token_raises_invalid_token_error() -> None:
    with pytest.raises(InvalidTokenError):
        verify_bearer_token(authorization="Bearer wrong-token", settings=_settings())


def test_unconfigured_auth_token_rejects_every_request() -> None:
    with pytest.raises(InvalidTokenError):
        verify_bearer_token(authorization="Bearer anything", settings=_settings(auth_token=""))
