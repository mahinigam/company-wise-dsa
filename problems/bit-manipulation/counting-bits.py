"""Counting Bits

Difficulty: Easy
Topic: bit-manipulation
Preparation tags (not verified question attribution): Microsoft, Amazon, Google
Source: https://leetcode.com/problems/counting-bits/

Problem summary: For every i from 0 through n, return the number of set bits in i.
Approach: Use dp[i] = dp[i >> 1] + (i & 1).
Complexity: O(n) time and O(n) output space.
"""

def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for value in range(1, n + 1):
        dp[value] = dp[value >> 1] + (value & 1)
    return dp

assert count_bits(2) == [0,1,1]
assert count_bits(5) == [0,1,1,2,1,2]
assert count_bits(0) == [0]
