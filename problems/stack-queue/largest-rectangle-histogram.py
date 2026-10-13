"""Largest Rectangle in Histogram

Difficulty: Hard
Topic: stack-queue
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem summary: Find the maximum rectangular area under histogram bars.
Approach: A monotonic stack finds the first shorter bar on each side for each candidate height.
Complexity: O(n) time and O(n) space.
"""

def largest_rectangle_area(heights: list[int]) -> int:
    stack = []; best = 0
    for i, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, h * (i - left - 1))
        stack.append(i)
    return best

assert largest_rectangle_area([2,1,5,6,2,3]) == 10
assert largest_rectangle_area([2,4]) == 4
assert largest_rectangle_area([]) == 0
