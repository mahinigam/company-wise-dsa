"""Reverse Integer

Difficulty: Medium
Topic: math
Preparation tags (not verified question attribution): Microsoft, Amazon, Accenture
Source: https://leetcode.com/problems/reverse-integer/

Problem summary: Reverse decimal digits and return zero if the result exceeds signed 32-bit range.
Approach: Reverse digits arithmetically and validate the signed integer bounds.
Complexity: O(log |x|) time and O(1) space.
"""

def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    value = abs(x); reversed_value = 0
    while value:
        reversed_value = reversed_value * 10 + value % 10
        value //= 10
    reversed_value *= sign
    return reversed_value if -(2**31) <= reversed_value <= 2**31 - 1 else 0

assert reverse_integer(123) == 321
assert reverse_integer(-123) == -321
assert reverse_integer(1534236469) == 0
