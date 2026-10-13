"""Palindrome Number

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/palindrome-number/

Problem summary: Check whether an integer reads the same forward and backward.
Approach: Reverse only the second half of the digits and compare halves.
Complexity: O(log n) time and O(1) space.
"""

def is_palindrome_number(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0): return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10

assert is_palindrome_number(121)
assert not is_palindrome_number(-121)
assert is_palindrome_number(10) is False
assert is_palindrome_number(0)
