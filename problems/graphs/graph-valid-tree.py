"""Graph Valid Tree

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Meta, Uber
Source: https://neetcode.io/problems/valid-tree

Problem summary: Check whether an undirected graph is connected and acyclic.
Approach: A valid tree has n-1 edges and one connected component; DFS verifies connectivity.
Complexity: O(V+E) time and O(V+E) space.
"""

def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if n == 0: return True
    if len(edges) != n - 1: return False
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b); graph[b].append(a)
    seen, stack = {0}, [0]
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt not in seen: seen.add(nxt); stack.append(nxt)
    return len(seen) == n

assert valid_tree(5, [[0,1],[0,2],[0,3],[1,4]])
assert not valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])
assert valid_tree(1, [])
