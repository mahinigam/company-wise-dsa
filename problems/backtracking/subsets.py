"""Subsets

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/subsets/

Problem summary: Return the power set of a list of distinct values.
Approach: At each index, either include the value or skip it.
Complexity: O(n·2^n) time and O(n) recursion space excluding output.
"""

def subsets(nums: list[int]) -> list[list[int]]:
    out = []
    def build(i, chosen):
        if i == len(nums):
            out.append(chosen[:]); return
        build(i + 1, chosen)
        chosen.append(nums[i]); build(i + 1, chosen); chosen.pop()
    build(0, [])
    return out

result = subsets([1, 2, 3])
assert len(result) == 8 and [] in result and [1, 2, 3] in result
assert subsets([]) == [[]]
