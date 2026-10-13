"""Letter Combinations of a Phone Number

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Meta, Uber
Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Problem summary: Return all letter strings represented by digits 2 through 9.
Approach: Backtrack over the mapped letters for each digit.
Complexity: O(4^n·n) time and O(n) recursion space excluding output.
"""

def letter_combinations(digits: str) -> list[str]:
    if not digits: return []
    mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    out = []
    def build(i, path):
        if i == len(digits): out.append("".join(path)); return
        for ch in mapping[int(digits[i])]:
            path.append(ch); build(i + 1, path); path.pop()
    build(0, [])
    return out

assert len(letter_combinations("23")) == 9
assert "ad" in letter_combinations("23") and "cf" in letter_combinations("23")
assert letter_combinations("") == []
