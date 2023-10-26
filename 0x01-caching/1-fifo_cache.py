#!/usr/bin/env python3
"""Inherits from BaseCaching and is a caching system"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO class to remove and get elements of a dictionary"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []
 
    def put(self, key, item):
        """Assigns elements to the dictionary"""
        if key is None or item is None:
            return
        if key not in self.queue:
            self.queue.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
            print("DISCARD: {}".format(first))

    def get(self, key):
        """Return the value of a key"""
        return self.cache_data.get(key, None)

    @staticmethod
    def get_first_list(array):
        """ Get first element of list or None """
        return array[0] if array else None
