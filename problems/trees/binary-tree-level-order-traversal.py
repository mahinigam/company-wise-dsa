"""Binary Tree Level Order Traversal

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/binary-tree-level-order-traversal/

Problem summary: Return node values level by level from top to bottom.
Approach: Use a queue and snapshot the queue length for each level.
Complexity: O(n) time and O(w) queue space, where w is maximum tree width.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None: return []
    queue, out = deque([root]), []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft(); level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(level)
    return out

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert level_order(root) == [[3], [9, 20], [15, 7]]
assert level_order(None) == []
