# http_client.py
"""HTTPClient: a small, reusable HTTP client built step by step across the
Requests, HTTPX, API Authentication, and Async Python lessons.

This is the HTTPX-lesson version: it keeps the synchronous `requests`-based
methods from the Requests lesson unchanged, and adds async methods backed
by `httpx.AsyncClient`, plus a bounded-concurrency batch runner. The next
lesson (API Authentication) extends this SAME class again, adding token
refresh and 401 retry.
"""

from __future__ import annotations

import asyncio
from typing import Any, Optional

import httpx
import requests


class HTTPClient:
    """A reusable HTTP client with sync (requests) and async (httpx) sides."""

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

    # ---- synchronous side (Requests lesson) ----

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        """Send a synchronous GET request relative to base_url."""
        kwargs.setdefault("timeout", self.timeout)
        return self._session.get(self._url(path), **kwargs)

    def post(self, path: str, json: Optional[dict] = None, **kwargs: Any) -> requests.Response:
        """Send a synchronous POST request with a JSON body."""
        kwargs.setdefault("timeout", self.timeout)
        return self._session.post(self._url(path), json=json, **kwargs)

    def close(self) -> None:
        """Release the underlying session's connections."""
        self._session.close()

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()

    # ---- asynchronous side (HTTPX lesson) ----

    async def aget(self, path: str, **kwargs: Any) -> httpx.Response:
        """Send an async GET request relative to base_url."""
        kwargs.setdefault("timeout", self.timeout)
        async with httpx.AsyncClient(headers=self._default_headers) as client:
            return await client.get(self._url(path), **kwargs)

    async def apost(self, path: str, json: Optional[dict] = None, **kwargs: Any) -> httpx.Response:
        """Send an async POST request with a JSON body."""
        kwargs.setdefault("timeout", self.timeout)
        async with httpx.AsyncClient(headers=self._default_headers) as client:
            return await client.post(self._url(path), json=json, **kwargs)

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
