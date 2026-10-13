"""Reorganize String

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/reorganize-string/

Problem summary: Rearrange characters so no equal adjacent characters remain, or return empty if impossible.
Approach: Greedily pop the most frequent available character while temporarily holding the previous one out of the heap.
Complexity: O(n log k) time and O(k) space.
"""

import heapq
from collections import Counter

def reorganize_string(s: str) -> str:
    counts = Counter(s)
    if max(counts.values(), default=0) > (len(s) + 1) // 2: return ""
    heap = [(-count, ch) for ch, count in counts.items()]
    heapq.heapify(heap); previous = (0, "")
    out = []
    while heap:
        count, ch = heapq.heappop(heap)
        out.append(ch)
        if previous[0] < 0: heapq.heappush(heap, previous)
        count += 1
        previous = (count, ch)
    result = "".join(out)
    return result if all(result[i] != result[i - 1] for i in range(1, len(result))) else ""

r = reorganize_string("aab"); assert len(r) == 3 and all(r[i] != r[i-1] for i in range(1, len(r)))
assert reorganize_string("aaab") == ""
assert reorganize_string("") == ""
