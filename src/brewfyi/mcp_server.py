"""MCP server for brewfyi — AI assistant tools for brewfyi.com.

Run: uvx --from "brewfyi[mcp]" python -m brewfyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BrewFYI")


@mcp.tool()
def list_brew_methods(limit: int = 20, offset: int = 0) -> str:
    """List brew_methods from brewfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        data = api.list_brew_methods(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No brew_methods found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_brew_method(slug: str) -> str:
    """Get detailed information about a specific brew_method.

    Args:
        slug: URL slug identifier for the brew_method.
    """
    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        data = api.get_brew_method(slug)
        return str(data)


@mcp.tool()
def list_species(limit: int = 20, offset: int = 0) -> str:
    """List species from brewfyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        data = api.list_species(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No species found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_brew(query: str) -> str:
    """Search brewfyi.com for coffee varieties, brew methods, and roasting.

    Args:
        query: Search query string.
    """
    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
