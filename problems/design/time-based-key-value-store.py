"""Time Based Key-Value Store

Difficulty: Medium
Topic: design
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/time-based-key-value-store/

Problem summary: Store values with timestamps and retrieve the latest value not later than a query time.
Approach: Keep each key's timestamped values in order and binary-search the last timestamp at most the query.
Complexity: O(log m) get and O(1) amortized set for ordered timestamps; O(n) space.
"""

from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.data = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        items = self.data.get(key, [])
        index = bisect_right(items, (timestamp, chr(0x10ffff))) - 1
        return items[index][1] if index >= 0 else ""

tm = TimeMap(); tm.set("foo", "bar", 1)
assert tm.get("foo", 1) == "bar" and tm.get("foo", 3) == "bar"
tm.set("foo", "bar2", 4); assert tm.get("foo", 4) == "bar2" and tm.get("foo", 0) == ""
