"""Regular Expression Matching

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/regular-expression-matching/

Problem summary: Match a string against a pattern containing '.' and '*' where '*' repeats the preceding token zero or more times.
Approach: DP over string and pattern prefixes; '*' either removes its preceding token or consumes another matching character.
Complexity: O(mn) time and O(mn) space.
"""

def is_match_regex(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == "*": dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] in (s[i - 1], "."): dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] in (s[i - 1], "."): dp[i][j] |= dp[i - 1][j]
    return dp[m][n]

assert is_match_regex("aa", "a*")
assert is_match_regex("ab", ".*")
assert not is_match_regex("mississippi", "mis*is*p*.")
