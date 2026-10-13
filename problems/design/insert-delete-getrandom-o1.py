"""Insert Delete GetRandom O(1)

Difficulty: Medium
Topic: design
Preparation tags (not verified question attribution): Meta, Google, Amazon
Source: https://leetcode.com/problems/insert-delete-getrandom-o1/

Problem summary: Support insert, remove, and uniform random retrieval in expected O(1) time.
Approach: Store values in a list and map values to indices; delete by swapping with the last value.
Complexity: Expected O(1) operations and O(n) space.
"""

import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index = {}
    def insert(self, val: int) -> bool:
        if val in self.index: return False
        self.index[val] = len(self.values); self.values.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index: return False
        i = self.index.pop(val)
        last = self.values.pop()
        if i < len(self.values):
            self.values[i] = last
            self.index[last] = i
        return True
    def get_random(self) -> int:
        if not self.values: raise IndexError("empty set")
        return random.choice(self.values)

rs = RandomizedSet(); assert rs.insert(1) and not rs.insert(1)
assert rs.insert(2) and rs.remove(1) and not rs.remove(1)
assert rs.get_random() == 2
