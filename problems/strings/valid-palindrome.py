"""Valid Palindrome

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe, Accenture
Source: https://leetcode.com/problems/valid-palindrome/

Problem summary: Check whether a string is a palindrome after lowercasing and discarding non-alphanumeric characters.
Approach: Move two pointers inward while skipping characters that are not letters or digits.
Complexity: O(n) time, O(1) extra space.
"""

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True

assert is_palindrome("A man, a plan, a canal: Panama")
assert not is_palindrome("race a car")
assert is_palindrome(" ")
