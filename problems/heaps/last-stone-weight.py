"""Last Stone Weight

Difficulty: Easy
Topic: heaps
Preparation tags (not verified question attribution): Amazon, Accenture, Target
Source: https://leetcode.com/problems/last-stone-weight/

Problem summary: Repeatedly smash the two heaviest stones and return the remaining weight.
Approach: Use a max-heap encoded with negative values.
Complexity: O(n log n) time, O(n) space.
"""

import heapq

def last_stone_weight(stones: list[int]) -> int:
    heap = [-x for x in stones]; heapq.heapify(heap)
    while len(heap) > 1:
        a, b = -heapq.heappop(heap), -heapq.heappop(heap)
        if a != b: heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0

assert last_stone_weight([2,7,4,1,8,1]) == 1
assert last_stone_weight([1]) == 1
assert last_stone_weight([3,3]) == 0
