"""Invert Binary Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Google, Microsoft, Amazon
Source: https://leetcode.com/problems/invert-binary-tree/

Problem summary: Swap every tree node's left and right subtrees.
Approach: Use DFS and recursively invert both children after swapping.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
invert_tree(root)
assert root.left.val == 7 and root.right.val == 2
assert root.left.left.val == 9 and root.left.right.val == 6
