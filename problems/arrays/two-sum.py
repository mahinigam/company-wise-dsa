"""Two Sum

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Google, Meta
Source: https://leetcode.com/problems/two-sum/

Problem summary: Return indices of two values whose sum equals the target.
Approach: Store each seen value's index and look for the complement before inserting the current value.
Complexity: O(n) time, O(n) extra space.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([], 3) == []
