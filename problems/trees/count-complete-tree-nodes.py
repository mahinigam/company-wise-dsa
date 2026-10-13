"""Count Complete Tree Nodes

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/count-complete-tree-nodes/

Problem summary: Count nodes in a complete binary tree.
Approach: Compare leftmost and rightmost heights; a perfect subtree's node count is known directly.
Complexity: O(log² n) time for a complete tree and O(log n) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def count_nodes(root: TreeNode | None) -> int:
    def left_height(node):
        height = 0
        while node: height += 1; node = node.left
        return height
    def right_height(node):
        height = 0
        while node: height += 1; node = node.right
        return height
    if root is None: return 0
    left, right = left_height(root), right_height(root)
    if left == right: return (1 << left) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
assert count_nodes(root) == 6
assert count_nodes(None) == 0
assert count_nodes(TreeNode(1)) == 1
