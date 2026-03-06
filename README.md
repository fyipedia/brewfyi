# brewfyi

[![PyPI](https://img.shields.io/pypi/v/brewfyi)](https://pypi.org/project/brewfyi/)
[![Python](https://img.shields.io/pypi/pyversions/brewfyi)](https://pypi.org/project/brewfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Coffee knowledge API client for Python. Search 72 coffee varieties, 20 origin countries, 21 brew methods, and coffee terminology from [BrewFYI](https://brewfyi.com) -- the complete coffee reference with 120 expert guides covering everything from Arabica genetics and processing methods to SCA cupping protocols and roast profiling.

> **Explore coffee at [brewfyi.com](https://brewfyi.com)** -- [Coffee Varieties](https://brewfyi.com/varieties/) | [Origins](https://brewfyi.com/origins/) | [Brew Methods](https://brewfyi.com/methods/) | [Coffee Guides](https://brewfyi.com/guides/)

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/brewfyi/main/demo.gif" alt="brewfyi demo -- coffee API search and lookup" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on BrewFYI](#what-youll-find-on-brewfyi)
  - [Coffee Species and Varieties](#coffee-species-and-varieties)
  - [Processing Methods](#processing-methods)
  - [Brew Methods](#brew-methods)
  - [Roast Levels](#roast-levels)
  - [Origin Countries](#origin-countries)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [API Client](#api-client)
- [Learn More About Coffee](#learn-more-about-coffee)
- [Beverage FYI Family](#beverage-fyi-family)
- [License](#license)

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
    # Search varieties, brew methods, origins, glossary terms
    results = api.search("espresso")
    print(results)

    # Look up a glossary term
    term = api.glossary_term("extraction")
    print(term["definition"])
```

## What You'll Find on BrewFYI

BrewFYI is a comprehensive coffee reference covering 72 coffee varieties, 20 origin countries, 21 brew methods, and 120 expert guides. The database spans the entire coffee journey -- from seed variety and terroir through processing, roasting, and extraction science.

### Coffee Species and Varieties

All commercial coffee comes from two primary species: **Coffea arabica** (60-70% of world production) and **Coffea canephora** (Robusta, 30-40%). Arabica is prized for its complex flavors and aromatic diversity, while Robusta offers higher caffeine content, greater disease resistance, and a stronger, more bitter profile often used in espresso blends.

BrewFYI catalogs 72 distinct varieties with genetic lineage, flavor profiles, and growing requirements:

| Category | Notable Varieties | Characteristics |
|----------|------------------|-----------------|
| Ethiopian Heirlooms | Gesha/Geisha, Yirgacheffe Landrace, Sidamo | Floral, jasmine, bergamot, complex acidity |
| Bourbon Lineage | Bourbon, Caturra, Catuai, Pacas, Villa Sarchi | Sweet, balanced, caramel, fruit notes |
| Typica Lineage | Typica, Maragogipe, Kona, Blue Mountain | Clean, sweet, mild body |
| Hybrid/Modern | Castillo, Colombia, Catimor, Sarchimor | Disease resistant, improving cup quality |
| Robusta | Robusta, Conilon | High caffeine, earthy, bitter, crema |

Learn more: [Browse Coffee Origins](https://brewfyi.com/origin/) · [Country Profiles](https://brewfyi.com/country/)

### Processing Methods

Post-harvest processing dramatically affects flavor. The same coffee cherry processed differently produces entirely different cup profiles:

| Method | Process | Flavor Impact |
|--------|---------|---------------|
| Washed (Wet) | Pulp removed, fermented, washed, dried | Clean, bright acidity, clarity of origin |
| Natural (Dry) | Whole cherry dried on raised beds | Fruity, wine-like, heavy body |
| Honey | Pulp removed, mucilage left during drying | Sweet, balanced, complex |
| Anaerobic | Sealed fermentation tanks, controlled environment | Intense, unique fermentation flavors |
| Wet-Hulled (Giling Basah) | Partially dried, hulled wet (Indonesia) | Earthy, low acidity, full body |

Learn more: [Processing Methods Guide](https://brewfyi.com/processing/) · [Coffee Glossary](https://brewfyi.com/glossary/)

### Brew Methods

BrewFYI covers 21 brewing methods with optimal parameters for water temperature, grind size, brew ratio, and extraction time. Each method extracts different compounds from ground coffee, producing distinct flavor profiles:

| Method | Type | Brew Time | Grind | Best For |
|--------|------|-----------|-------|----------|
| Espresso | Pressure (9 bar) | 25-30s | Fine | Concentrated, crema, milk drinks |
| Pour Over (V60) | Drip/Percolation | 2:30-3:30 | Medium-fine | Clarity, origin character |
| French Press | Immersion | 4:00 | Coarse | Full body, oils, texture |
| AeroPress | Pressure/Immersion | 1:00-2:00 | Medium-fine | Versatile, clean, portable |
| Cold Brew | Cold immersion | 12-24h | Coarse | Smooth, low acidity, sweet |
| Moka Pot | Steam pressure | 4-5 min | Fine-medium | Strong, stovetop espresso |
| Chemex | Drip/Percolation | 3:30-4:30 | Medium-coarse | Clean, bright, paper filtered |
| Siphon | Vacuum | 1:30-2:00 | Medium | Theatrical, clean, aromatic |

Learn more: [21 Brew Methods](https://brewfyi.com/method/) · [Brewing Tools](https://brewfyi.com/tools/)

### Roast Levels

Roast level determines the balance between origin character and roast-developed flavors. Lighter roasts preserve acidity and origin terroir; darker roasts emphasize body, bitterness, and caramelization:

| Level | Internal Temp | Characteristics |
|-------|--------------|-----------------|
| Light | 180-205C | Bright acidity, floral, fruity, tea-like body |
| Medium-Light | 210-220C | Balanced, caramel sweetness, origin + roast |
| Medium | 220-230C | Balanced body, chocolate, nuts, rounded acidity |
| Medium-Dark | 230-240C | Bittersweet, cocoa, reduced acidity, fuller body |
| Dark | 240C+ | Smoky, bitter, oily surface, minimal origin character |

Learn more: [Roast Level Guide](https://brewfyi.com/roast/) · [Coffee Guides](https://brewfyi.com/guide/)

### Origin Countries

Coffee is grown in the "Bean Belt" between the Tropics of Cancer and Capricorn. BrewFYI covers 20 origin countries with altitude ranges, harvest seasons, typical processing methods, and regional flavor profiles.

Top producers include Brazil (world's largest), Vietnam (Robusta leader), Colombia, Ethiopia (birthplace of coffee), Indonesia, Honduras, India, Uganda, Mexico, and Guatemala. Specialty coffee increasingly highlights single-origin and micro-lot traceable sourcing.

Learn more: [Browse Coffee Origins](https://brewfyi.com/origin/) · [Country Profiles](https://brewfyi.com/country/)

## API Endpoints

All endpoints are free, require no authentication, and return JSON with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/varieties/` | List all 72 coffee varieties |
| GET | `/api/v1/varieties/{slug}/` | Variety detail with genetics, flavor |
| GET | `/api/v1/origins/` | List all 20 origin countries |
| GET | `/api/v1/origins/{slug}/` | Origin detail with altitude, harvest |
| GET | `/api/v1/methods/` | List all 21 brew methods |
| GET | `/api/v1/methods/{slug}/` | Brew method detail with parameters |
| GET | `/api/v1/glossary/` | List all coffee terminology |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two varieties or methods |
| GET | `/api/v1/random/` | Random variety or method |
| GET | `/api/v1/guides/` | List all 120 guides |
| GET | `/api/v1/guides/{slug}/` | Guide detail |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
curl -s "https://brewfyi.com/api/v1/varieties/gesha/"
```

```json
{
  "slug": "gesha",
  "name": "Gesha",
  "species": "arabica",
  "description": "Legendary Ethiopian variety prized for its extraordinary floral aromatics, jasmine and bergamot notes, and tea-like body.",
  "origin": "Gori Gesha forest, Ethiopia",
  "flavor_profile": ["jasmine", "bergamot", "peach", "tropical fruit", "honey"],
  "altitude_range": "1,500-2,000m",
  "processing": ["washed", "natural", "honey"],
  "url": "https://brewfyi.com/varieties/gesha/"
}
```

Full API documentation: [brewfyi.com/developers/](https://brewfyi.com/developers/).
OpenAPI 3.1.0 spec: [brewfyi.com/api/v1/openapi.json](https://brewfyi.com/api/v1/openapi.json).

## Command-Line Interface

```bash
# Search varieties, brew methods, origins
brewfyi search "espresso"
brewfyi search "pour over"
brewfyi search "arabica"
brewfyi search "ethiopia"

# Look up coffee terminology
brewfyi term "extraction"
brewfyi term "channeling"
brewfyi term "crema"
```

The CLI displays results in formatted tables with rich terminal output.

## MCP Server (Claude, Cursor, Windsurf)

Run as an MCP server for AI-assisted coffee queries:

```bash
python -m brewfyi.mcp_server
```

**Claude Desktop** (`~/.claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "brewfyi": {
      "command": "uvx",
      "args": ["--from", "brewfyi[mcp]", "python", "-m", "brewfyi.mcp_server"]
    }
  }
}
```

**Tools**: `coffee_search`, `coffee_glossary_term`

## API Client

```python
from brewfyi.api import BrewFYI

with BrewFYI() as api:
    # Search across varieties, origins, methods, glossary
    results = api.search("espresso")

    # Look up coffee terminology
    term = api.glossary_term("channeling")
    print(term["definition"])

    # Compare two brew methods
    comparison = api.compare("v60", "chemex")

    # Get a random variety
    random_variety = api.random()
```

## Learn More About Coffee

- **Reference**: [Coffee Varieties](https://brewfyi.com/varieties/) | [Origins](https://brewfyi.com/origins/) | [Brew Methods](https://brewfyi.com/methods/)
- **Glossary**: [Coffee Terminology](https://brewfyi.com/glossary/)
- **Guides**: [Coffee Guides](https://brewfyi.com/guides/)
- **Compare**: [Variety Comparisons](https://brewfyi.com/compare/)
- **API**: [Developer Docs](https://brewfyi.com/developers/) | [OpenAPI Spec](https://brewfyi.com/api/v1/openapi.json)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- world beverages from cocktails to sake.

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktails, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, BJCP |
| **BrewFYI** | [brewfyi.com](https://brewfyi.com) | **72 coffee varieties, roasting, 21 brew methods** |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## License

MIT
