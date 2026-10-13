"""Longest Subarray With Sum K

Difficulty: Medium
Topic: prefix-sums
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

Problem summary: Find the maximum length of a contiguous subarray with sum k.
Approach: Store the first index of each prefix sum, which works with negative values.
Complexity: O(n) expected time, O(n) space.
"""

def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    earliest, prefix, best = {0: -1}, 0, 0
    for i, value in enumerate(nums):
        prefix += value
        if prefix - k in earliest: best = max(best, i - earliest[prefix - k])
        earliest.setdefault(prefix, i)
    return best

assert longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15) == 4
assert longest_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4
assert longest_subarray_sum_k([], 0) == 0
