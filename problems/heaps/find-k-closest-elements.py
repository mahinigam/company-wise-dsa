"""Find K Closest Elements

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/find-k-closest-elements/

Problem summary: Return k values closest to x in a sorted array, preferring smaller values on ties.
Approach: Order by absolute distance and value, then sort the selected values.
Complexity: O(n log n) time, O(n) space in this clear baseline.
"""

def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    if not 0 <= k <= len(arr): raise ValueError("k out of range")
    return sorted(sorted(arr, key=lambda value: (abs(value - x), value))[:k])

assert find_closest_elements([1,2,3,4,5], 4, 3) == [1,2,3,4]
assert find_closest_elements([1,2,3,4,5], 4, -1) == [1,2,3,4]
assert find_closest_elements([], 0, 10) == []
