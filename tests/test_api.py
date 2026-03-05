"""Tests for brewfyi.api — API client initialization and URL construction."""

from brewfyi.api import BrewFYI


class TestBrewFYIInit:
    def test_default_base_url(self) -> None:
        client = BrewFYI()
        assert str(client._client.base_url) == "https://brewfyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = BrewFYI(base_url="https://custom.example.com")
        assert str(client._client.base_url) == "https://custom.example.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = BrewFYI()
        assert client._client.timeout.read == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = BrewFYI(timeout=30.0)
        assert client._client.timeout.read == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with BrewFYI() as api:
            assert isinstance(api, BrewFYI)


class TestURLConstruction:
    def test_search_url(self) -> None:
        """Verify search endpoint path without making HTTP calls."""
        client = BrewFYI()
        req = client._client.build_request("GET", "/api/search/", params={"q": "espresso"})
        assert str(req.url) == "https://brewfyi.com/api/search/?q=espresso"
        client.close()

    def test_search_url_encoding(self) -> None:
        """Verify URL encoding for search queries with spaces."""
        client = BrewFYI()
        req = client._client.build_request("GET", "/api/search/", params={"q": "pour over"})
        assert "q=pour" in str(req.url)
        assert "over" in str(req.url)
        client.close()
