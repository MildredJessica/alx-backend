#!/usr/bin/env python3
"""Inherits from BaseCaching and is a caching system"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO class to remove and get elements of a dictionary"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assigns elements to the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """Return the value of a key"""
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)
