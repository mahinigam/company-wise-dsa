"""Reverse Words in a String

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/reverse-words-in-a-string/

Problem summary: Reverse word order and normalize spaces.
Approach: Split on arbitrary whitespace, reverse the word list, and join with one space.
Complexity: O(n) time and O(n) space.
"""

def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))

assert reverse_words("the sky is blue") == "blue is sky the"
assert reverse_words("  hello world  ") == "world hello"
assert reverse_words("a good   example") == "example good a"
