"""Minimum ASCII Delete Sum for Two Strings

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Problem summary: Find the minimum sum of deleted character codes to make two strings equal.
Approach: DP over prefixes: matching characters inherit diagonal cost; otherwise delete one side at its character cost.
Complexity: O(mn) time and O(n) space.
"""

def minimum_delete_sum(s1: str, s2: str) -> int:
    dp = [0] * (len(s2) + 1)
    for j, ch in enumerate(s2, 1): dp[j] = dp[j - 1] + ord(ch)
    for a in s1:
        previous = dp[0]; dp[0] += ord(a)
        for j, b in enumerate(s2, 1):
            old = dp[j]
            dp[j] = previous if a == b else min(dp[j] + ord(a), dp[j - 1] + ord(b))
            previous = old
    return dp[-1]

assert minimum_delete_sum("sea", "eat") == 231
assert minimum_delete_sum("delete", "leet") == 403
assert minimum_delete_sum("", "a") == 97
