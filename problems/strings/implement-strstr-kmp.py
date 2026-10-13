"""Find the Index of the First Occurrence

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Problem summary: Return the first occurrence of needle in haystack, or -1.
Approach: Use the Knuth–Morris–Pratt prefix table to avoid rescanning matched characters.
Complexity: O(n+m) time and O(m) space.
"""

def str_str(haystack: str, needle: str) -> int:
    if not needle: return 0
    lps = [0] * len(needle); j = 0
    for i in range(1, len(needle)):
        while j and needle[i] != needle[j]: j = lps[j - 1]
        if needle[i] == needle[j]: j += 1; lps[i] = j
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1; j += 1
            if j == len(needle): return i - j
        elif j: j = lps[j - 1]
        else: i += 1
    return -1

assert str_str("sadbutsad", "sad") == 0
assert str_str("leetcode", "leeto") == -1
assert str_str("abc", "") == 0
