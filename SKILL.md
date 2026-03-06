---
name: coffee-tools
description: Search 72 coffee varieties, 20 origin countries, 21 brew methods, and coffee terminology from BrewFYI. Use when answering questions about coffee species, processing methods, brew techniques, roast levels, or extraction science.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://brewfyi.com/"
---

# BrewFYI -- Coffee Tools for AI Agents

Coffee knowledge API client for Python. Search 72 coffee varieties, 20 origin countries, 21 brew methods, and coffee terminology from BrewFYI -- the comprehensive coffee reference with 120 expert guides covering Arabica genetics, processing methods, SCA cupping protocols, and roast profiling.

**Install**: `pip install brewfyi[api]` -- **Web**: [brewfyi.com](https://brewfyi.com/) -- **API**: [REST API](https://brewfyi.com/developers/) -- **PyPI**: [brewfyi](https://pypi.org/project/brewfyi/)

## When to Use

- User asks about coffee varieties, species, or genetic lineage (Arabica vs Robusta)
- User needs brew method parameters (temperature, grind, ratio, time)
- User wants coffee origin profiles (altitude, harvest, processing)
- User asks about processing methods (washed, natural, honey, anaerobic)
- User needs roast level guidance or cupping terminology

## Tools

### `BrewFYI` API Client

HTTP client for the brewfyi.com REST API. Requires `pip install brewfyi[api]`.

```python
from brewfyi.api import BrewFYI

with BrewFYI() as api:
    results = api.search("espresso")   # Search varieties, methods, origins, glossary
```

**Methods:**
- `search(query: str) -> dict` -- Search coffee varieties, brew methods, and glossary terms

## REST API (No Auth Required)

```bash
# Search
curl "https://brewfyi.com/api/v1/search/?q=espresso"

# Variety detail
curl "https://brewfyi.com/api/v1/varieties/gesha/"

# Brew method detail
curl "https://brewfyi.com/api/v1/methods/pour-over/"

# Glossary term
curl "https://brewfyi.com/api/v1/glossary/extraction/"

# Compare two varieties
curl "https://brewfyi.com/api/v1/compare/gesha/bourbon/"
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/varieties/` | List all 72 coffee varieties |
| GET | `/api/v1/varieties/{slug}/` | Variety detail with genetics, flavor |
| GET | `/api/v1/origins/` | List all 20 origin countries |
| GET | `/api/v1/origins/{slug}/` | Origin detail with altitude, harvest |
| GET | `/api/v1/methods/` | List all 21 brew methods |
| GET | `/api/v1/methods/{slug}/` | Brew method detail with parameters |
| GET | `/api/v1/glossary/{slug}/` | Glossary term definition |
| GET | `/api/v1/search/?q={query}` | Search across all content |
| GET | `/api/v1/compare/{slug1}/{slug2}/` | Compare two varieties or methods |
| GET | `/api/v1/random/` | Random variety or method |
| GET | `/api/v1/openapi.json` | OpenAPI 3.1.0 specification |

Full spec: [OpenAPI 3.1.0](https://brewfyi.com/api/v1/openapi.json)

## Coffee Species and Varieties

| Category | Notable Varieties | Characteristics |
|----------|------------------|-----------------|
| Ethiopian Heirlooms | Gesha/Geisha, Yirgacheffe Landrace | Floral, jasmine, bergamot, complex acidity |
| Bourbon Lineage | Bourbon, Caturra, Catuai, Pacas | Sweet, balanced, caramel, fruit notes |
| Typica Lineage | Typica, Maragogipe, Kona, Blue Mountain | Clean, sweet, mild body |
| Hybrid/Modern | Castillo, Colombia, Catimor | Disease resistant, improving cup quality |
| Robusta | Robusta, Conilon | High caffeine, earthy, bitter, crema |

## Processing Methods

| Method | Flavor Impact |
|--------|---------------|
| Washed (Wet) | Clean, bright acidity, clarity of origin |
| Natural (Dry) | Fruity, wine-like, heavy body |
| Honey | Sweet, balanced, complex |
| Anaerobic | Intense, unique fermentation flavors |
| Wet-Hulled | Earthy, low acidity, full body |

## Brew Methods

| Method | Type | Brew Time | Grind |
|--------|------|-----------|-------|
| Espresso | Pressure (9 bar) | 25-30s | Fine |
| Pour Over (V60) | Drip/Percolation | 2:30-3:30 | Medium-fine |
| French Press | Immersion | 4:00 | Coarse |
| AeroPress | Pressure/Immersion | 1:00-2:00 | Medium-fine |
| Cold Brew | Cold immersion | 12-24h | Coarse |

## Demo

![BrewFYI demo](https://raw.githubusercontent.com/fyipedia/brewfyi/main/demo.gif)

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
