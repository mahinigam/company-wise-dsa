"""First Unique Character

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Adobe, Accenture
Source: https://leetcode.com/problems/first-unique-character-in-a-string/

Problem summary: Return the index of the first non-repeating character, or -1.
Approach: Count characters then scan from left to right.
Complexity: O(n) time, O(k) space.
"""

from collections import Counter

def first_uniq_char(s: str) -> int:
    counts = Counter(s)
    return next((i for i, ch in enumerate(s) if counts[ch] == 1), -1)

assert first_uniq_char("leetcode") == 0
assert first_uniq_char("loveleetcode") == 2
assert first_uniq_char("aabb") == -1
