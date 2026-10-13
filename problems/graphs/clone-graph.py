"""Clone Graph

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/clone-graph/

Problem summary: Deep-copy a connected undirected graph.
Approach: DFS with a map from original node identity to its clone prevents cycles and preserves shared neighbours.
Complexity: O(V+E) time and O(V) space.
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val, self.neighbors = val, neighbors or []

def clone_graph(node: Node | None) -> Node | None:
    if node is None: return None
    clones = {}
    def copy(original):
        if original in clones: return clones[original]
        cloned = Node(original.val)
        clones[original] = cloned
        cloned.neighbors = [copy(neighbor) for neighbor in original.neighbors]
        return cloned
    return copy(node)

a, b = Node(1), Node(2); a.neighbors = [b]; b.neighbors = [a]
copy_a = clone_graph(a)
assert copy_a is not a and copy_a.val == 1
assert copy_a.neighbors[0] is not b and copy_a.neighbors[0].neighbors[0] is copy_a
assert clone_graph(None) is None
