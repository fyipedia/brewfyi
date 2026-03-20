"""HTTP API client for brewfyi.com REST endpoints.

Requires the ``api`` extra: ``pip install brewfyi[api]``

Usage::

    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        items = api.list_brew_methods()
        detail = api.get_brew_method("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class BrewFYI:
    """API client for the brewfyi.com REST API.

    Provides typed access to all brewfyi.com endpoints including
    list, detail, and search operations.

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

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_brew_methods(self, **params: Any) -> dict[str, Any]:
        """List all brew methods."""
        return self._get("/api/v1/brew-methods/", **params)

    def get_brew_method(self, slug: str) -> dict[str, Any]:
        """Get brew method by slug."""
        return self._get(f"/api/v1/brew-methods/" + slug + "/")

    def list_countries(self, **params: Any) -> dict[str, Any]:
        """List all countries."""
        return self._get("/api/v1/countries/", **params)

    def get_country(self, slug: str) -> dict[str, Any]:
        """Get country by slug."""
        return self._get(f"/api/v1/countries/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_processing_methods(self, **params: Any) -> dict[str, Any]:
        """List all processing methods."""
        return self._get("/api/v1/processing-methods/", **params)

    def get_processing_method(self, slug: str) -> dict[str, Any]:
        """Get processing method by slug."""
        return self._get(f"/api/v1/processing-methods/" + slug + "/")

    def list_regions(self, **params: Any) -> dict[str, Any]:
        """List all regions."""
        return self._get("/api/v1/regions/", **params)

    def get_region(self, slug: str) -> dict[str, Any]:
        """Get region by slug."""
        return self._get(f"/api/v1/regions/" + slug + "/")

    def list_roast_levels(self, **params: Any) -> dict[str, Any]:
        """List all roast levels."""
        return self._get("/api/v1/roast-levels/", **params)

    def get_roast_level(self, slug: str) -> dict[str, Any]:
        """Get roast level by slug."""
        return self._get(f"/api/v1/roast-levels/" + slug + "/")

    def list_species(self, **params: Any) -> dict[str, Any]:
        """List all species."""
        return self._get("/api/v1/species/", **params)

    def get_specy(self, slug: str) -> dict[str, Any]:
        """Get specy by slug."""
        return self._get(f"/api/v1/species/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_varieties(self, **params: Any) -> dict[str, Any]:
        """List all varieties."""
        return self._get("/api/v1/varieties/", **params)

    def get_variety(self, slug: str) -> dict[str, Any]:
        """Get variety by slug."""
        return self._get(f"/api/v1/varieties/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> BrewFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
