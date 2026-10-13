"""LRU Cache

Difficulty: Medium
Topic: design
Preparation tags (not verified question attribution): Amazon, Google, Meta, Uber
Source: https://leetcode.com/problems/lru-cache/

Problem summary: Implement a cache with O(1) get/put and least-recently-used eviction.
Approach: Python's OrderedDict keeps recency order while supporting O(1) moves and eviction.
Complexity: O(1) average per operation, O(capacity) space.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0: raise ValueError("capacity must be non-negative")
        self.capacity = capacity
        self.data = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.data: return -1
        self.data.move_to_end(key)
        return self.data[key]
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.data: self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity: self.data.popitem(last=False)

cache = LRUCache(2); cache.put(1,1); cache.put(2,2)
assert cache.get(1) == 1
cache.put(3,3); assert cache.get(2) == -1
cache.put(4,4); assert cache.get(1) == -1 and cache.get(3) == 3 and cache.get(4) == 4
