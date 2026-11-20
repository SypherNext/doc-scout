"""Bearer-token authentication for every route except ``/health`` and ``/docs``.

Follows the API Authentication lesson's bearer-token pattern: a single,
configurable token compared against the ``Authorization`` header. Simple,
stateless, no user database -- appropriate for a service-to-service API
with no per-user auth needs (see the Capstone Reference Architecture's auth
decision).
"""

from __future__ import annotations

from fastapi import Depends, Header

from research_assistant.config import Settings, load_config
from research_assistant.exceptions import InvalidTokenError, MissingTokenError

_BEARER_PREFIX = "Bearer "


def verify_bearer_token(
    authorization: str | None = Header(default=None),
    settings: Settings = Depends(load_config),
) -> str:
    """FastAPI dependency: extract and verify the bearer token.

    Args:
        authorization: Raw ``Authorization`` header value, injected by FastAPI.
        settings: Application settings, for the configured ``auth_token``.

    Returns:
        The verified token, for handlers that want to log it (never log the
        token itself -- this is provided for request correlation, not logging).

    Raises:
        MissingTokenError: No ``Authorization`` header was sent, or it did
            not use the ``Bearer`` scheme. The route handler for this maps
            to HTTP 401.
        InvalidTokenError: A token was sent but it does not match the
            configured value. Maps to HTTP 403.
    """
    if not authorization or not authorization.startswith(_BEARER_PREFIX):
        raise MissingTokenError("Missing or malformed Authorization header")

    token = authorization[len(_BEARER_PREFIX) :].strip()
    if not token:
        raise MissingTokenError("Missing or malformed Authorization header")

    if not settings.auth_token or token != settings.auth_token:
        raise InvalidTokenError("Bearer token does not match the configured AUTH_TOKEN")

    return token
