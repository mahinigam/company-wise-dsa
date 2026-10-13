"""Wildcard Matching

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/wildcard-matching/

Problem summary: Match a string against a pattern where '?' matches one character and '*' matches any sequence.
Approach: Greedily remember the last star and retry from it when a character mismatch appears.
Complexity: O(mn) worst-case time and O(1) space.
"""

def is_match_wildcard(s: str, p: str) -> bool:
    i = j = 0; star = -1; retry = 0
    while i < len(s):
        if j < len(p) and (p[j] == "?" or p[j] == s[i]):
            i += 1; j += 1
        elif j < len(p) and p[j] == "*":
            star = j; retry = i; j += 1
        elif star != -1:
            j = star + 1; retry += 1; i = retry
        else: return False
    while j < len(p) and p[j] == "*": j += 1
    return j == len(p)

assert not is_match_wildcard("aa", "a")
assert is_match_wildcard("aa", "*")
assert is_match_wildcard("cb", "?a") is False
assert is_match_wildcard("adceb", "*a*b")
