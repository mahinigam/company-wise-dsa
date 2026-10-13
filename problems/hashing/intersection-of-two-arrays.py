"""Intersection of Two Arrays

Difficulty: Easy
Topic: hashing
Preparation tags (not verified question attribution): Amazon, Microsoft, Target
Source: https://leetcode.com/problems/intersection-of-two-arrays/

Problem summary: Return the distinct values shared by two arrays.
Approach: Intersect sets and return a stable sorted result.
Complexity: O(n + m) expected time plus O(r log r) to sort r results.
"""

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return sorted(set(nums1).intersection(nums2))


assert intersection([1, 2, 2, 1], [2, 2]) == [2]
assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
