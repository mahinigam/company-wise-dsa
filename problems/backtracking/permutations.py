"""Permutations

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/permutations/

Problem summary: Return all permutations of distinct values.
Approach: Backtrack by choosing an unused value at each position.
Complexity: O(n·n!) time and O(n) recursion space excluding output.
"""

def permute(nums: list[int]) -> list[list[int]]:
    out = []; path = []; used = [False] * len(nums)
    def search():
        if len(path) == len(nums): out.append(path[:]); return
        for i, value in enumerate(nums):
            if used[i]: continue
            used[i] = True; path.append(value)
            search()
            path.pop(); used[i] = False
    search()
    return out

assert {tuple(x) for x in permute([1,2,3])} == {(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)}
assert permute([]) == [[]]
