"""Ransom Note

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Meta, Adobe
Source: https://leetcode.com/problems/ransom-note/

Problem summary: Check whether magazine characters can form the ransom note.
Approach: Count available characters and ensure each requested count is available.
Complexity: O(n + m) time and O(k) space.
"""

from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    available = Counter(magazine)
    needed = Counter(ransom_note)
    return all(available[ch] >= count for ch, count in needed.items())


assert can_construct("aa", "aab")
assert not can_construct("aa", "ab")
assert can_construct("", "")
