"""Edit Distance

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/edit-distance/

Problem summary: Find the minimum insertions, deletions, and replacements to transform one word into another.
Approach: DP over prefixes; equal characters inherit the diagonal, otherwise add one to the best edit operation.
Complexity: O(mn) time and O(min(m,n)) space.
"""

def min_distance(word1: str, word2: str) -> int:
    if len(word2) > len(word1): word1, word2 = word2, word1
    dp = list(range(len(word2) + 1))
    for i, a in enumerate(word1, 1):
        diagonal = dp[0]; dp[0] = i
        for j, b in enumerate(word2, 1):
            above = dp[j]
            dp[j] = diagonal if a == b else 1 + min(diagonal, dp[j], dp[j - 1])
            diagonal = above
    return dp[-1]

assert min_distance("horse", "ros") == 3
assert min_distance("intention", "execution") == 5
assert min_distance("", "abc") == 3
