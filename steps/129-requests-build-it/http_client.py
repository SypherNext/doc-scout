# http_client.py
"""HTTPClient: a small, reusable HTTP client built step by step across the
Requests, HTTPX, API Authentication, and Async Python lessons.

This is the Requests-lesson version: a synchronous client backed by a
`requests.Session`, with a base URL, default headers, and a timeout
applied to every call. Later lessons extend this SAME class instead of
writing a new one-off client.
"""

from __future__ import annotations

from typing import Any, Optional

import requests


class HTTPClient:
    """A reusable HTTP client with a persistent session and sane defaults."""

    def __init__(
        self,
        base_url: str,
        headers: Optional[dict] = None,
        timeout: float = 10.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self._default_headers = {"Content-Type": "application/json"}
        if headers:
            self._default_headers.update(headers)

        self._session = requests.Session()
        self._session.headers.update(self._default_headers)

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        """Send a GET request relative to base_url."""
        kwargs.setdefault("timeout", self.timeout)
        return self._session.get(self._url(path), **kwargs)

    def post(self, path: str, json: Optional[dict] = None, **kwargs: Any) -> requests.Response:
        """Send a POST request with a JSON body relative to base_url."""
        kwargs.setdefault("timeout", self.timeout)
        return self._session.post(self._url(path), json=json, **kwargs)

    def close(self) -> None:
        """Release the underlying session's connections."""
        self._session.close()

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()
