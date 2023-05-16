#!/usr/bin/env python3
"""
BasicCache module
"""

from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """

    def put(self, key: Any, item: Any) -> None:
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
