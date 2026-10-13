"""Pow(x, n)

Difficulty: Medium
Topic: math
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/powx-n/

Problem summary: Compute x raised to integer power n.
Approach: Exponentiation by squaring halves the exponent each step; invert x for negative powers.
Complexity: O(log |n|) time and O(1) space.
"""

def my_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1: result *= x
        x *= x; n >>= 1
    return result

assert abs(my_pow(2.0, 10) - 1024.0) < 1e-9
assert abs(my_pow(2.1, 3) - 9.261) < 1e-9
assert abs(my_pow(2.0, -2) - 0.25) < 1e-9
