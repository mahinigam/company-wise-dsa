"""Isomorphic Strings

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Adobe, Target
Source: https://leetcode.com/problems/isomorphic-strings/

Problem summary: Check whether two strings have a consistent one-to-one character mapping.
Approach: Maintain forward and reverse maps so no two source characters map to the same target.
Complexity: O(n) time, O(k) space.
"""

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    forward, reverse = {}, {}
    for a, b in zip(s, t):
        if forward.get(a, b) != b or reverse.get(b, a) != a: return False
        forward[a], reverse[b] = b, a
    return True

assert is_isomorphic("egg", "add")
assert not is_isomorphic("foo", "bar")
assert is_isomorphic("paper", "title")
