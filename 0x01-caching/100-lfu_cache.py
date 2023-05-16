#!/usr/bin/env python3
"""
LFUCache module
"""

from typing import Any
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def put(self, key: Any, item: Any) -> None:
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item  # Update existing key
            self.frequency[key] += 1  # Increment frequency
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.discard_items()  # Discard items if cache is full

            self.cache_data[key] = item
            self.frequency[key] = 1  # Set initial frequency to 1
            self.min_frequency = 1  # Update min_frequency

    def get(self, key: Any) -> Any:
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1  # Increment frequency
        return self.cache_data[key]

    def discard_items(self):
        """ Discard least frequency used items """
        least_frequent_keys = [
            key for key in self.cache_data if self.frequency[key] == self.min_frequency
        ]
        least_recently_used_key = min(
            least_frequent_keys, key=lambda key: self.timestamp.get(key, 0)
        )
        del self.cache_data[least_recently_used_key]
        del self.frequency[least_recently_used_key]
        self.timestamp.pop(least_recently_used_key, None)
        print("DISCARD:", least_recently_used_key)

        if not least_frequent_keys:
            self.min_frequency += 1
