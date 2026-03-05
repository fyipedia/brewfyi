"""HTTP API client for brewfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install brewfyi[api]``

Usage::

    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        results = api.search("espresso")
        print(results)
"""

from __future__ import annotations

from typing import Any

import httpx


class BrewFYI:
    """API client for the brewfyi.com REST API.

    Args:
        base_url: API base URL. Defaults to ``https://brewfyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://brewfyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def search(self, query: str) -> dict[str, Any]:
        """Search coffee varieties, brew methods, and glossary terms.

        Args:
            query: Search term (e.g. ``"espresso"``, ``"arabica"``).
        """
        return self._get("/api/search/", q=query)

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> BrewFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
