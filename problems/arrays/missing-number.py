"""Missing Number

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/missing-number/

Problem summary: Find the absent value from the range 0 through n.
Approach: Subtract the array sum from the expected arithmetic-series sum.
Complexity: O(n) time and O(1) extra space.
"""

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


assert missing_number([3, 0, 1]) == 2
assert missing_number([0, 1]) == 2
assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
