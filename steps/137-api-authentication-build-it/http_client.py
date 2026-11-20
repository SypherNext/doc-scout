# http_client.py
"""HTTPClient: a small, reusable HTTP client built step by step across the
Requests, HTTPX, API Authentication, and Async Python lessons.

This is the final version, extended by the API Authentication lesson:
- A static `api_key` is sent as a bearer token on every request.
- An optional `token_provider` callable returns a fresh (token, expires_in)
  pair; the client calls it before the token expires and retries once on
  a 401 in case the token expired mid-flight.

The Async Python lesson adds no new capability: it uses `aget`/`apost`/
`run_concurrent` exactly as they are here, for real concurrent HTTP calls
instead of `asyncio.sleep()` simulations.
"""

from __future__ import annotations

import asyncio
import time
from typing import Any, Callable, Optional

import httpx
import requests

TokenProvider = Callable[[], tuple[str, float]]


class HTTPClient:
    """A reusable HTTP client with sync/async transport and bearer auth."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        headers: Optional[dict] = None,
        timeout: float = 10.0,
        token_provider: Optional[TokenProvider] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.api_key = api_key
        self.token_provider = token_provider
        self._token_expires_at = 0.0

        self._default_headers = {"Content-Type": "application/json"}
        if headers:
            self._default_headers.update(headers)

        self._session = requests.Session()
        self._session.headers.update(self._default_headers)
        if self.api_key:
            self._session.headers["Authorization"] = f"Bearer {self.api_key}"

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _refresh_if_needed(self) -> None:
        """Fetch a new token from token_provider if the cached one expired."""
        if self.token_provider and time.time() >= self._token_expires_at:
            token, expires_in = self.token_provider()
            self.api_key = token
            self._token_expires_at = time.time() + expires_in - 60  # 60s buffer
            self._session.headers["Authorization"] = f"Bearer {token}"

    def _auth_headers(self) -> dict:
        headers = dict(self._default_headers)
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    # ---- synchronous side (Requests + API Authentication lessons) ----

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        """Send a synchronous GET request, refreshing/retrying auth as needed."""
        return self._request("GET", path, **kwargs)

    def post(self, path: str, json: Optional[dict] = None, **kwargs: Any) -> requests.Response:
        """Send a synchronous POST request, refreshing/retrying auth as needed."""
        return self._request("POST", path, json=json, **kwargs)

    def _request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        self._refresh_if_needed()
        kwargs.setdefault("timeout", self.timeout)
        response = self._session.request(method, self._url(path), **kwargs)

        if response.status_code == 401 and self.token_provider:
            # Token may have expired mid-flight: force a refresh and retry once.
            self._token_expires_at = 0.0
            self._refresh_if_needed()
            response = self._session.request(method, self._url(path), **kwargs)

        return response

    def close(self) -> None:
        """Release the underlying session's connections."""
        self._session.close()

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()

    # ---- asynchronous side (HTTPX + API Authentication + Async Python lessons) ----

    async def aget(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send an async GET request, refreshing/retrying auth as needed."""
        return await self._arequest("GET", path, **kwargs)

    async def apost(self, path: str, json: Optional[dict] = None, **kwargs: Any) -> httpx.Response:
        """Send an async POST request, refreshing/retrying auth as needed."""
        return await self._arequest("POST", path, json=json, **kwargs)

    async def _arequest(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        self._refresh_if_needed()
        kwargs.setdefault("timeout", self.timeout)

        async with httpx.AsyncClient(headers=self._auth_headers()) as client:
            response = await client.request(method, self._url(path), **kwargs)

            if response.status_code == 401 and self.token_provider:
                self._token_expires_at = 0.0
                self._refresh_if_needed()
                response = await client.request(
                    method, self._url(path), headers=self._auth_headers(), **kwargs
                )

            return response

    async def run_concurrent(
        self,
        requests_spec: list[tuple[str, str, Optional[dict]]],
        max_concurrent: int = 5,
    ) -> list[Any]:
        """Run many requests concurrently with bounded concurrency.

        `requests_spec` is a list of (method, path, json_body) tuples.
        Exceptions are captured as values, not raised, so one failure
        does not lose the other results.
        """
        sem = asyncio.Semaphore(max_concurrent)

        async def one(method: str, path: str, body: Optional[dict]) -> httpx.Response:
            async with sem:
                if method.upper() == "GET":
                    return await self.aget(path)
                return await self.apost(path, json=body)

        tasks = [one(method, path, body) for method, path, body in requests_spec]
        return await asyncio.gather(*tasks, return_exceptions=True)
