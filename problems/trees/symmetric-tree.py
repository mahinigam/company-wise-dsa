"""Symmetric Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/symmetric-tree/

Problem summary: Check whether a tree mirrors itself around its center.
Approach: Compare outer and inner pairs recursively.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_symmetric(root: TreeNode | None) -> bool:
    def mirror(a, b):
        if a is None or b is None: return a is b
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
    return True if root is None else mirror(root.left, root.right)

assert is_symmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
assert not is_symmetric(TreeNode(1, TreeNode(2), TreeNode(2, None, TreeNode(3))))
