"""Find All Anagrams in a String

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Meta, Google, Amazon
Source: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Problem summary: Return every start index of a substring that is an anagram of p.
Approach: Maintain a fixed-length count window and compare it with p's frequency map.
Complexity: O(n·k) worst case for Counter comparison; O(k) space.
"""

from collections import Counter

def find_anagrams(s: str, p: str) -> list[int]:
    width = len(p)
    if width == 0 or width > len(s): return []
    target = Counter(p)
    window = Counter(s[:width])
    out = [0] if window == target else []
    for right in range(width, len(s)):
        window[s[right]] += 1
        left_char = s[right - width]
        window[left_char] -= 1
        if window[left_char] == 0: del window[left_char]
        if window == target: out.append(right - width + 1)
    return out

assert find_anagrams("cbaebabacd", "abc") == [0, 6]
assert find_anagrams("abab", "ab") == [0, 1, 2]
assert find_anagrams("abc", "") == []
