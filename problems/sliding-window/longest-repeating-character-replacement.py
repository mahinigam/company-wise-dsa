"""Longest Repeating Character Replacement

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Meta, Google, Amazon
Source: https://leetcode.com/problems/longest-repeating-character-replacement/

Problem summary: Find the longest substring that can be made of one repeated uppercase letter using at most k replacements.
Approach: Maintain a window whose length minus its highest character frequency is at most k.
Complexity: O(n) time and O(1) space for a fixed alphabet.
"""

def character_replacement(s: str, k: int) -> int:
    counts = {}
    left = best = max_count = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_count = max(max_count, counts[ch])
        while right - left + 1 - max_count > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

assert character_replacement("ABAB", 2) == 4
assert character_replacement("AABABBA", 1) == 4
assert character_replacement("", 2) == 0
