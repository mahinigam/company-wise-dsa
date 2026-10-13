"""Kth Largest Element in an Array

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem summary: Return the kth largest value, counting duplicates.
Approach: Use a min-heap of size k so its root is the kth largest among processed values.
Complexity: O(n log k) time and O(k) extra space.
"""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums): raise ValueError("k out of range")
    return heapq.nlargest(k, nums)[-1]

assert find_kth_largest([3,2,1,5,6,4], 2) == 5
assert find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
