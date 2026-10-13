"""Binary Tree Right Side View

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Meta, Microsoft
Source: https://leetcode.com/problems/binary-tree-right-side-view/

Problem summary: Return the node visible at each level from the right side.
Approach: Perform level-order traversal and record the last node in each level.
Complexity: O(n) time and O(w) queue space.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None: return []
    queue, out = deque([root]), []
    while queue:
        last = None
        for _ in range(len(queue)):
            node = queue.popleft(); last = node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        out.append(last)
    return out

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
assert right_side_view(root) == [1, 3, 4]
assert right_side_view(None) == []
