"""Command-line interface for brewfyi.

Requires the ``cli`` extra: ``pip install brewfyi[cli]``

Usage::

    brewfyi search "espresso"
    brewfyi search "pour over"
"""

from __future__ import annotations

from typing import Any

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="brewfyi",
    help="Coffee knowledge API client — search coffee varieties, brew methods, and terms.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'espresso', 'arabica', 'pour over')"),
    base_url: str = typer.Option("https://brewfyi.com", "--base-url", help="API base URL"),
) -> None:
    """Search coffee varieties, brew methods, and glossary terms."""
    from brewfyi.api import BrewFYI

    with BrewFYI(base_url=base_url) as api:
        data = api.search(query)

    results: list[dict[str, Any]] = data.get("results", [])
    if not results:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name", style="bold")
    table.add_column("URL")

    for item in results:
        table.add_row(
            item.get("type", ""),
            item.get("name", ""),
            item.get("url", ""),
        )

    console.print(table)


if __name__ == "__main__":
    app()
