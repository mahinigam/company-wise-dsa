"""Power of Two

Difficulty: Easy
Topic: bit-manipulation
Preparation tags (not verified question attribution): Amazon, Microsoft, Accenture
Source: https://leetcode.com/problems/power-of-two/

Problem summary: Determine whether an integer is a positive power of two.
Approach: Positive powers of two have exactly one set bit.
Complexity: O(1) time and space for fixed-width integers.
"""

def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

assert is_power_of_two(1)
assert is_power_of_two(16)
assert not is_power_of_two(3)
assert not is_power_of_two(0)
