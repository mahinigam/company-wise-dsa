"""Subarray Sum Equals K

Difficulty: Medium
Topic: prefix-sums
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/subarray-sum-equals-k/

Problem summary: Count contiguous subarrays whose sum is k, even when values may be negative.
Approach: Use prefix-sum frequencies; each prefix contributes prior prefixes equal to current-k.
Complexity: O(n) expected time, O(n) space.
"""

from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    freq = defaultdict(int, {0: 1})
    prefix = answer = 0
    for value in nums:
        prefix += value
        answer += freq[prefix - k]
        freq[prefix] += 1
    return answer

assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, 2, 3], 3) == 2
assert subarray_sum([1, -1, 0], 0) == 3
