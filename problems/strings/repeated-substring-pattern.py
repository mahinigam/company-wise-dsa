"""Repeated Substring Pattern

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Adobe, Target
Source: https://leetcode.com/problems/repeated-substring-pattern/

Problem summary: Determine whether a string is a repetition of a shorter substring.
Approach: A nontrivial repeated string appears inside the doubled string after trimming its ends.
Complexity: O(n) time and O(n) space.
"""

def repeated_substring_pattern(s: str) -> bool:
    return len(s) > 1 and s in (s + s)[1:-1]

assert repeated_substring_pattern("abab")
assert repeated_substring_pattern("abcabcabc")
assert not repeated_substring_pattern("aba")
