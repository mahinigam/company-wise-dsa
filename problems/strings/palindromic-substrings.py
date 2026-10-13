"""Palindromic Substrings

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/palindromic-substrings/

Problem summary: Count every palindromic substring, including equal substrings at different positions.
Approach: Expand around each odd and even center, counting each successful expansion.
Complexity: O(n²) time and O(1) space.
"""

def count_substrings(s: str) -> int:
    count = 0
    for center in range(len(s)):
        for left0, right0 in ((center, center), (center, center + 1)):
            left, right = left0, right0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1; left -= 1; right += 1
    return count

assert count_substrings("abc") == 3
assert count_substrings("aaa") == 6
assert count_substrings("") == 0
