"""Majority Element

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Google
Source: https://leetcode.com/problems/majority-element/

Problem summary: Find the element appearing more than half the time; such an element is guaranteed to exist.
Approach: Use the Boyer–Moore voting algorithm to cancel different values.
Complexity: O(n) time and O(1) extra space.
"""

def majority_element(nums: list[int]) -> int:
    candidate = None
    balance = 0
    for value in nums:
        if balance == 0:
            candidate = value
        balance += 1 if value == candidate else -1
    return candidate  # input guarantee ensures a majority exists


assert majority_element([3, 2, 3]) == 3
assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
