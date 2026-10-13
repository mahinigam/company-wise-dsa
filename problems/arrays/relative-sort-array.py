"""Relative Sort Array

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Adobe, Target
Source: https://leetcode.com/problems/relative-sort-array/

Problem summary: Sort arr1 so values in arr2 appear first in arr2 order; sort remaining values ascending.
Approach: Count arr1 values, emit arr2 values in order, then emit remaining values sorted.
Complexity: O(n log n) time and O(k) extra space.
"""

from collections import Counter

def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = Counter(arr1); out = []
    for value in arr2:
        out.extend([value] * counts.pop(value, 0))
    for value in sorted(counts):
        out.extend([value] * counts[value])
    return out

assert relative_sort_array([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
assert relative_sort_array([1,2,3], []) == [1,2,3]
