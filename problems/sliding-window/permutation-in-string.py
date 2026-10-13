"""Permutation in String

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Meta, Amazon, Google
Source: https://leetcode.com/problems/permutation-in-string/

Problem summary: Check whether s1's permutation appears as a substring of s2.
Approach: Compare character counts for a sliding window of fixed length.
Complexity: O(n) time and O(k) space.
"""

from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    width = len(s1)
    if width > len(s2): return False
    need = Counter(s1)
    window = Counter(s2[:width])
    if window == need: return True
    for i in range(width, len(s2)):
        window[s2[i]] += 1
        old = s2[i - width]
        window[old] -= 1
        if window[old] == 0: del window[old]
        if window == need: return True
    return width == 0

assert check_inclusion("ab", "eidbaooo")
assert not check_inclusion("ab", "eidboaoo")
assert check_inclusion("", "abc")
