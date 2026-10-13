"""Longest Common Subsequence

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/longest-common-subsequence/

Problem summary: Find the length of the longest subsequence shared by two strings.
Approach: DP over prefixes: matching characters extend the diagonal; otherwise choose the better neighbour.
Complexity: O(mn) time and O(n) space.
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    if len(text2) > len(text1): text1, text2 = text2, text1
    dp = [0] * (len(text2) + 1)
    for a in text1:
        previous = 0
        for j, b in enumerate(text2, 1):
            old = dp[j]
            dp[j] = previous + 1 if a == b else max(dp[j], dp[j - 1])
            previous = old
    return dp[-1]

assert longest_common_subsequence("abcde", "ace") == 3
assert longest_common_subsequence("abc", "abc") == 3
assert longest_common_subsequence("abc", "def") == 0
