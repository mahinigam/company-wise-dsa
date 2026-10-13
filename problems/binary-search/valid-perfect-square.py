"""Valid Perfect Square

Difficulty: Easy
Topic: binary-search
Preparation tags (not verified question attribution): Microsoft, Amazon, Accenture
Source: https://leetcode.com/problems/valid-perfect-square/

Problem summary: Check whether a positive integer is a perfect square without using a square-root function.
Approach: Binary-search an integer whose square equals num.
Complexity: O(log n) time and O(1) space.
"""

def is_perfect_square(num: int) -> bool:
    if num < 0: return False
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num: return True
        if square < num: left = mid + 1
        else: right = mid - 1
    return False

assert is_perfect_square(16)
assert not is_perfect_square(14)
assert is_perfect_square(0)
