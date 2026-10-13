"""Redundant Connection

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/redundant-connection/

Problem summary: Find the edge that creates a cycle in a graph that began as a tree.
Approach: Use disjoint-set union; the first edge joining vertices already in one set is redundant.
Complexity: O(E α(V)) amortized time and O(V) space.
"""

def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    n = max(max(edge) for edge in edges)
    parent = list(range(n + 1)); size = [1] * (n + 1)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb: return [a, b]
        if size[ra] < size[rb]: ra, rb = rb, ra
        parent[rb] = ra; size[ra] += size[rb]
    return []

assert find_redundant_connection([[1,2],[1,3],[2,3]]) == [2,3]
assert find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
