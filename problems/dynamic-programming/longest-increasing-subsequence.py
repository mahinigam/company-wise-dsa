"""Longest Increasing Subsequence

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/longest-increasing-subsequence/

Problem summary: Find the length of the longest strictly increasing subsequence.
Approach: Maintain minimal tail values and binary-search where each number belongs.
Complexity: O(n log n) time and O(n) space.
"""

from bisect import bisect_left

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for value in nums:
        i = bisect_left(tails, value)
        if i == len(tails): tails.append(value)
        else: tails[i] = value
    return len(tails)

assert length_of_lis([10,9,2,5,3,7,101,18]) == 4
assert length_of_lis([0,1,0,3,2,3]) == 4
assert length_of_lis([7,7,7,7]) == 1
