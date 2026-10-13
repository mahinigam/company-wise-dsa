"""Sqrt(x)

Difficulty: Easy
Topic: binary-search
Preparation tags (not verified question attribution): Accenture, Amazon, Microsoft
Source: https://leetcode.com/problems/sqrtx/

Problem summary: Return the floor of the square root of a non-negative integer.
Approach: Binary search for the greatest integer whose square is at most x.
Complexity: O(log x) time and O(1) space.
"""

def my_sqrt(x: int) -> int:
    if x < 2: return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x: return mid
        if square < x: left = mid + 1
        else: right = mid - 1
    return right

assert my_sqrt(4) == 2
assert my_sqrt(8) == 2
assert my_sqrt(0) == 0
