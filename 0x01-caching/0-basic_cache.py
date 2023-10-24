#!/usr/bin/env python3
"""  BasicCache Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""
    def put(self, key, item):
        """Must assign to the dictionary """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data[key]"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
