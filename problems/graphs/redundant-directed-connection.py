"""Redundant Connection II

Difficulty: Hard
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/redundant-connection-ii/

Problem summary: Remove one directed edge so the remaining graph is a rooted tree.
Approach: Detect a node with two parents, then use DSU to determine which candidate edge completes a cycle.
Complexity: O(n α(n)) time and O(n) space.
"""

def find_redundant_directed_connection(edges: list[list[int]]) -> list[int]:
    n = len(edges); parent = [0] * (n + 1)
    earlier = later = None
    for u, v in edges:
        if parent[v]:
            earlier = [parent[v], v]; later = [u, v]
            break
        parent[v] = u
    dsu = list(range(n + 1))
    def find(x):
        while dsu[x] != x:
            dsu[x] = dsu[dsu[x]]; x = dsu[x]
        return x
    for edge in edges:
        if edge == later: continue
        u, v = edge; ru, rv = find(u), find(v)
        if ru == rv: return earlier if earlier else edge
        dsu[rv] = ru
    return later if later else []

assert find_redundant_directed_connection([[1,2],[1,3],[2,3]]) == [2,3]
assert find_redundant_directed_connection([[1,2],[2,3],[3,4],[4,1],[1,5]]) == [4,1]
