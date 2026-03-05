"""brewfyi — Coffee knowledge API client for developers.

Search coffee varieties, brew methods, and terminology from BrewFYI.

Usage::

    from brewfyi.api import BrewFYI

    with BrewFYI() as api:
        results = api.search("espresso")
        print(results)
"""

__version__ = "0.1.0"
