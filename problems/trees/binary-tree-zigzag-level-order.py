"""Binary Tree Zigzag Level Order Traversal

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Problem summary: Return level-order values, alternating left-to-right and right-to-left.
Approach: Use BFS and reverse every other collected level.
Complexity: O(n) time and O(w) queue space.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None: return []
    queue, out, reverse = deque([root]), [], False
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft(); level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(level[::-1] if reverse else level)
        reverse = not reverse
    return out

assert zigzag_level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3], [20, 9], [15, 7]]
assert zigzag_level_order(None) == []
