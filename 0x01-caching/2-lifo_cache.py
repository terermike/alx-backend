#!/usr/bin/env python3
"""
LIFOCache module
"""

from typing import Any
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.stack = []

    def put(self, key: Any, item: Any) -> None:
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key: Any) -> Any:
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
