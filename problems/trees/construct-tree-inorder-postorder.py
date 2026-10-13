"""Construct Binary Tree From Inorder and Postorder

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Problem summary: Rebuild a binary tree from inorder and postorder traversals with unique values.
Approach: Read postorder backward and build right subtree before left using inorder boundaries.
Complexity: O(n) time and O(n) space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    positions = {value: i for i, value in enumerate(inorder)}
    cursor = len(postorder) - 1
    def build(lo, hi):
        nonlocal cursor
        if lo >= hi: return None
        value = postorder[cursor]; cursor -= 1
        node = TreeNode(value); mid = positions[value]
        node.right = build(mid + 1, hi); node.left = build(lo, mid)
        return node
    if len(inorder) != len(postorder): raise ValueError("traversals must have equal lengths")
    return build(0, len(inorder))

root = build_tree([9,3,15,20,7], [9,15,7,20,3])
assert root.val == 3 and root.left.val == 9 and root.right.left.val == 15
assert build_tree([], []) is None
