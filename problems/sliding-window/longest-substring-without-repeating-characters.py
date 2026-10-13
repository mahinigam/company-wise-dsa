"""Longest Substring Without Repeating Characters

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Amazon, Meta, Google, Uber
Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem summary: Find the maximum length of a substring with all unique characters.
Approach: Track the last index of each character and move the window's left edge past duplicates.
Complexity: O(n) time and O(k) space.
"""

def length_of_longest_substring(s: str) -> int:
    last = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last: left = max(left, last[ch] + 1)
        last[ch] = right
        best = max(best, right - left + 1)
    return best

assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("") == 0
