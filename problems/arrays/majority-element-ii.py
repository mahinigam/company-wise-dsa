"""Majority Element II

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/majority-element-ii/

Problem summary: Return values occurring more than floor(n/3) times.
Approach: Use the extended Boyer–Moore method with at most two candidates, then verify counts.
Complexity: O(n) time, O(1) auxiliary space.
"""

def majority_element_ii(nums: list[int]) -> list[int]:
    a = b = None
    ca = cb = 0
    for x in nums:
        if x == a: ca += 1
        elif x == b: cb += 1
        elif ca == 0: a, ca = x, 1
        elif cb == 0: b, cb = x, 1
        else: ca -= 1; cb -= 1
    threshold = len(nums) // 3
    return [x for x in (a, b) if x is not None and nums.count(x) > threshold and (x == a or x != a)]

assert set(majority_element_ii([3, 2, 3])) == {3}
assert set(majority_element_ii([1])) == {1}
assert majority_element_ii([1, 2, 3, 4]) == []
