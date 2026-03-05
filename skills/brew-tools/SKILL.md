---
name: brew-tools
description: Search coffee cultivars, roasting profiles, brewing methods, and SCA cupping protocol data for specialty coffee professionals.
---

# Brew Tools

Coffee search and reference powered by [brewfyi](https://brewfyi.com/) -- a comprehensive coffee knowledge platform covering cultivars, processing methods, roasting science, and SCA cupping protocols.

## Setup

Install the MCP server:

```bash
pip install "brewfyi[mcp]"
```

Add to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "brewfyi": {
            "command": "python",
            "args": ["-m", "brewfyi.mcp_server"]
        }
    }
}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `coffee_search` | Search coffee cultivars, origins, processing methods, roast profiles, and terminology |

## When to Use

- Looking up coffee cultivars (Typica, Bourbon, Geisha, SL28, etc.)
- Researching processing methods (washed, natural, honey, anaerobic)
- Exploring roast profiles and Maillard reaction chemistry
- Finding brewing method parameters (pour-over, espresso, cold brew, AeroPress)
- Understanding SCA cupping protocol and scoring

## Links

- [Coffee Cultivars](https://brewfyi.com/cultivars/)
- [Processing Methods](https://brewfyi.com/processing/)
- [Brewing Methods](https://brewfyi.com/methods/)
- [API Documentation](https://brewfyi.com/developers/)
- [PyPI Package](https://pypi.org/project/brewfyi/)
