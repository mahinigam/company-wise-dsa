"""Next Greater Element I

Difficulty: Easy
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Google, Target
Source: https://leetcode.com/problems/next-greater-element-i/

Problem summary: For each query value, find the next greater value to its right in a reference array.
Approach: Build a value-to-next-greater map with a decreasing stack.
Complexity: O(n+m) time and O(n) space.
"""

def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    stack, nxt = [], {}
    for value in nums2:
        while stack and stack[-1] < value:
            nxt[stack.pop()] = value
        stack.append(value)
    return [nxt.get(value, -1) for value in nums1]

assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
