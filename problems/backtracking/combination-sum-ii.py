"""Combination Sum II

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/combination-sum-ii/

Problem summary: Find unique combinations summing to target when each candidate can be used at most once.
Approach: Sort candidates and skip duplicates at the same recursion depth.
Complexity: Exponential worst-case time; O(n) recursion space.
"""

def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort(); out = []
    def search(start, remaining, path):
        if remaining == 0: out.append(path[:]); return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]: continue
            value = candidates[i]
            if value > remaining: break
            path.append(value); search(i + 1, remaining - value, path); path.pop()
    search(0, target, [])
    return out

assert {tuple(x) for x in combination_sum2([10,1,2,7,6,1,5], 8)} == {(1,1,6),(1,2,5),(1,7),(2,6)}
assert combination_sum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
