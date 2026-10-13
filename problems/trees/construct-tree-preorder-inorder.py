"""Construct Binary Tree From Preorder and Inorder

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem summary: Reconstruct a binary tree from its preorder and inorder traversals with unique values.
Approach: Preorder identifies each root; an inorder index map separates its left and right subtrees.
Complexity: O(n) time and O(n) space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    positions = {value: i for i, value in enumerate(inorder)}
    cursor = 0
    def build(lo, hi):
        nonlocal cursor
        if lo >= hi: return None
        value = preorder[cursor]; cursor += 1
        root = TreeNode(value)
        mid = positions[value]
        root.left = build(lo, mid)
        root.right = build(mid + 1, hi)
        return root
    if len(preorder) != len(inorder): raise ValueError("traversals must have equal lengths")
    return build(0, len(inorder))

root = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
assert root.val == 3 and root.left.val == 9 and root.right.left.val == 15
assert build_tree([], []) is None
