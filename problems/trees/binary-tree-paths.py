"""Binary Tree Paths

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/binary-tree-paths/

Problem summary: Return every root-to-leaf path formatted as values separated by arrows.
Approach: DFS carries the path prefix and emits it at each leaf.
Complexity: O(n·h) output-sensitive time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def binary_tree_paths(root: TreeNode | None) -> list[str]:
    out = []
    def visit(node, path):
        if node is None: return
        path = path + [str(node.val)]
        if node.left is None and node.right is None:
            out.append("->".join(path)); return
        visit(node.left, path); visit(node.right, path)
    visit(root, [])
    return out

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
assert set(binary_tree_paths(root)) == {"1->2->5", "1->3"}
assert binary_tree_paths(None) == []
