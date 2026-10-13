"""Minimum Window Substring

Difficulty: Hard
Topic: sliding-window
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/minimum-window-substring/

Problem summary: Find the smallest substring of s containing all characters of t with multiplicity.
Approach: Expand until all required characters are covered, then shrink the left boundary as far as possible.
Complexity: O(|s|+|t|) time and O(k) space.
"""

from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s): return ""
    need = Counter(t); missing = len(t); left = 0
    best_left, best_len = 0, float("inf")
    for right, ch in enumerate(s):
        if need[ch] > 0: missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_left, best_len = left, right - left + 1
            need[s[left]] += 1
            if need[s[left]] > 0: missing += 1
            left += 1
    return "" if best_len == float("inf") else s[best_left:best_left + best_len]

assert min_window("ADOBECODEBANC", "ABC") == "BANC"
assert min_window("a", "a") == "a"
assert min_window("a", "aa") == ""
