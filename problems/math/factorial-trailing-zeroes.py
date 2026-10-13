"""Factorial Trailing Zeroes

Difficulty: Medium
Topic: math
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/factorial-trailing-zeroes/

Problem summary: Count trailing zero digits in n factorial.
Approach: Each zero requires a factor of 10; count powers of 5 in n!.
Complexity: O(log n) time and O(1) space.
"""

def trailing_zeroes(n: int) -> int:
    count = 0
    while n:
        n //= 5
        count += n
    return count

assert trailing_zeroes(3) == 0
assert trailing_zeroes(5) == 1
assert trailing_zeroes(100) == 24
