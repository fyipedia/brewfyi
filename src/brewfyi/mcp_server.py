"""MCP server for brewfyi — coffee knowledge tools for AI assistants.

Requires the ``mcp`` extra: ``pip install brewfyi[mcp]``

Run as a standalone server::

    python -m brewfyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "brewfyi": {
                "command": "python",
                "args": ["-m", "brewfyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("brewfyi")


@mcp.tool()
def coffee_search(query: str) -> str:
    """Search coffee varieties, brew methods, and glossary terms from BrewFYI.

    Search the BrewFYI coffee encyclopedia for varieties, brewing methods,
    origins, processing methods, roasting levels, flavors, and terminology.

    Args:
        query: Search term (e.g. "espresso", "arabica", "pour over", "chemex").
    """
    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        data = api.search(query)

    results: list[dict[str, Any]] = data.get("results", [])
    if not results:
        return f"No results found for '{query}'."

    lines = [
        f"## Coffee Search: {query}",
        "",
        f"Found {len(results)} result(s):",
        "",
        "| Type | Name | URL |",
        "|------|------|-----|",
    ]
    for item in results:
        item_type = item.get("type", "")
        name = item.get("name", "")
        url = item.get("url", "")
        lines.append(f"| {item_type} | {name} | {url} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
