"""Shortest Common Supersequence

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/shortest-common-supersequence/

Problem summary: Return the shortest string containing both input strings as subsequences.
Approach: Build LCS lengths, then reconstruct by including shared characters once and the remaining unmatched characters.
Complexity: O(mn) time and O(mn) space.
"""

def shortest_common_supersequence(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if str1[i] == str2[j] else max(dp[i + 1][j], dp[i][j + 1])
    i = j = 0; out = []
    while i < m and j < n:
        if str1[i] == str2[j]:
            out.append(str1[i]); i += 1; j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            out.append(str1[i]); i += 1
        else:
            out.append(str2[j]); j += 1
    out.extend(str1[i:]); out.extend(str2[j:])
    return "".join(out)

result = shortest_common_supersequence("abac", "cab")
assert len(result) == 5 and all(ch in result for ch in "abac") and all(ch in result for ch in "cab")
