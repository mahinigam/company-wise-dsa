"""Subtree of Another Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/subtree-of-another-tree/

Problem summary: Determine whether subRoot occurs as a subtree of root.
Approach: At each node, check structural equality; otherwise recurse to both children.
Complexity: O(n·m) worst case, O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    def same(a, b):
        if a is None or b is None: return a is b
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
    if sub_root is None: return True
    if root is None: return False
    return same(root, sub_root) or is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

assert is_subtree(TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), TreeNode(4, TreeNode(1), TreeNode(2)))
assert not is_subtree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(2, None, TreeNode(4)))
