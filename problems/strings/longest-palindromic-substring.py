"""Longest Palindromic Substring

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/longest-palindromic-substring/

Problem summary: Return the longest palindromic substring.
Approach: Expand around each character and each gap as a potential center.
Complexity: O(n²) time and O(1) extra space.
"""

def longest_palindrome(s: str) -> str:
    best = ""
    for center in range(len(s)):
        for left0, right0 in ((center, center), (center, center + 1)):
            left, right = left0, right0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1; right += 1
            if right - left - 1 > len(best): best = s[left + 1:right]
    return best

assert longest_palindrome("babad") in {"bab", "aba"}
assert longest_palindrome("cbbd") == "bb"
assert longest_palindrome("") == ""
