"""Number of Connected Components

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Meta, Uber
Source: https://neetcode.io/problems/count-connected-components

Problem summary: Count connected components in an undirected graph with n labelled vertices.
Approach: Use disjoint-set union to merge endpoints and count successful merges from n components.
Complexity: O((V+E) α(V)) amortized time and O(V) space.
"""

def count_components(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n)); size = [1] * n
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    components = n
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb: continue
        if size[ra] < size[rb]: ra, rb = rb, ra
        parent[rb] = ra; size[ra] += size[rb]; components -= 1
    return components

assert count_components(5, [[0,1],[1,2],[3,4]]) == 2
assert count_components(1, []) == 1
assert count_components(4, []) == 4
