"""Palindrome Partitioning

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/palindrome-partitioning/

Problem summary: Partition a string so every substring is a palindrome.
Approach: Try each palindromic prefix, then recurse on the remaining suffix.
Complexity: Exponential output-sensitive time; O(n) recursion space excluding output.
"""

def partition_palindromes(s: str) -> list[list[str]]:
    out = []
    def search(start, path):
        if start == len(s): out.append(path[:]); return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:
                path.append(piece); search(end, path); path.pop()
    search(0, [])
    return out

assert {tuple(x) for x in partition_palindromes("aab")} == {("a","a","b"),("aa","b")}
assert partition_palindromes("") == [[]]
