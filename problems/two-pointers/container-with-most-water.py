"""Container With Most Water

Difficulty: Medium
Topic: two-pointers
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/container-with-most-water/

Problem summary: Find the largest area formed by two vertical lines and the x-axis.
Approach: Move the pointer at the shorter line because the other side cannot improve its limiting height.
Complexity: O(n) time, O(1) space.
"""

def max_area(height: list[int]) -> int:
    left, right, best = 0, len(height) - 1, 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]: left += 1
        else: right -= 1
    return best

assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1, 1]) == 1
assert max_area([]) == 0
