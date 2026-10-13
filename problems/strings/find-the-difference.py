"""Find the Difference

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Adobe, Accenture
Source: https://leetcode.com/problems/find-the-difference/

Problem summary: Find the extra character added to t after shuffling s.
Approach: XOR character code points so matching characters cancel.
Complexity: O(n) time and O(1) space.
"""

def find_the_difference(s: str, t: str) -> str:
    result = 0
    for ch in s + t: result ^= ord(ch)
    return chr(result)

assert find_the_difference("abcd", "abcde") == "e"
assert find_the_difference("", "y") == "y"
