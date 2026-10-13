"""Alien Dictionary

Difficulty: Hard
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://neetcode.io/problems/foreign-dictionary

Problem summary: Infer a character order from a sorted list of words in an unknown alphabet.
Approach: Compare adjacent words to add one ordering edge, then topologically sort all characters.
Complexity: O(total characters + alphabet edges) time and space.
"""

from collections import defaultdict, deque

def alien_order(words: list[str]) -> str:
    graph = {ch: set() for word in words for ch in word}
    indegree = {ch: 0 for ch in graph}
    for first, second in zip(words, words[1:]):
        if len(first) > len(second) and first.startswith(second): return ""
        for a, b in zip(first, second):
            if a != b:
                if b not in graph[a]: graph[a].add(b); indegree[b] += 1
                break
    queue = deque(sorted(ch for ch, degree in indegree.items() if degree == 0))
    order = []
    while queue:
        ch = queue.popleft(); order.append(ch)
        for nxt in sorted(graph[ch]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0: queue.append(nxt)
    return "".join(order) if len(order) == len(graph) else ""

result = alien_order(["wrt","wrf","er","ett","rftt"])
assert result.index("w") < result.index("e") < result.index("r") < result.index("t") < result.index("f")
assert alien_order(["abc","ab"]) == ""
assert alien_order(["z","x","z"]) == ""
