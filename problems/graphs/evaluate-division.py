"""Evaluate Division

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/evaluate-division/

Problem summary: Evaluate ratio queries using a graph of known variable relationships.
Approach: Represent a/b=w and b/a=1/w as weighted edges; DFS multiplies edge weights along a path.
Complexity: O(Q·(V+E)) worst case and O(V+E) space.
"""

from collections import defaultdict

def calc_equation(equations, values, queries):
    graph = defaultdict(list)
    for (a, b), value in zip(equations, values):
        graph[a].append((b, value)); graph[b].append((a, 1 / value))
    def query(src, dst):
        if src not in graph or dst not in graph: return -1.0
        if src == dst: return 1.0
        stack = [(src, 1.0)]; seen = {src}
        while stack:
            node, product = stack.pop()
            if node == dst: return product
            for nxt, weight in graph[node]:
                if nxt not in seen:
                    seen.add(nxt); stack.append((nxt, product * weight))
        return -1.0
    return [query(a, b) for a, b in queries]

ans = calc_equation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
assert ans[:2] == [6.0, 0.5] and ans[2:] == [-1.0, 1.0, -1.0]
