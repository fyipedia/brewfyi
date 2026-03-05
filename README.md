# brewfyi

Coffee knowledge API client for developers — search coffee varieties, brew methods, and terms from [BrewFYI](https://brewfyi.com).

## Install

```bash
pip install brewfyi[api]     # API client (httpx)
pip install brewfyi[cli]     # + CLI (typer, rich)
pip install brewfyi[mcp]     # + MCP server
pip install brewfyi[all]     # Everything
```

## Quick Start

```python
from brewfyi.api import BrewFYI

with BrewFYI() as api:
    results = api.search("espresso")
    print(results)
```

## CLI

```bash
brewfyi search "espresso"
brewfyi search "pour over"
brewfyi search "arabica"
```

## MCP Server

```bash
# Add to Claude Desktop config
python -m brewfyi.mcp_server
```

Tools: `coffee_search`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `search(query)` | `GET /api/search/?q=...` | Search varieties, methods, terms |

## Links

- [BrewFYI](https://brewfyi.com) — Coffee encyclopedia with varieties, brew methods, and origins
- [PyPI](https://pypi.org/project/brewfyi/)
- [GitHub](https://github.com/fyipedia/brewfyi)
- [FYIPedia](https://fyipedia.com) — Open-source developer tools ecosystem
