"""Valid Anagram

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Adobe, Accenture, Target
Source: https://leetcode.com/problems/valid-anagram/

Problem summary: Check whether two strings contain the same characters with the same frequencies.
Approach: Compare character frequency maps.
Complexity: O(n + m) time and O(k) space for k distinct characters.
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


assert is_anagram("anagram", "nagaram")
assert not is_anagram("rat", "car")
assert is_anagram("", "")
