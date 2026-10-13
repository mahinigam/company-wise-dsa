"""Balanced Binary Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/balanced-binary-tree/

Problem summary: Check whether every node's subtree heights differ by at most one.
Approach: Return height bottom-up and use -1 as an early unbalanced sentinel.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_balanced(root: TreeNode | None) -> bool:
    def height(node):
        if node is None: return 0
        left = height(node.left)
        if left == -1: return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1: return -1
        return 1 + max(left, right)
    return height(root) != -1

assert is_balanced(TreeNode(1, TreeNode(2), TreeNode(3)))
assert not is_balanced(TreeNode(1, TreeNode(2, TreeNode(3))))
assert is_balanced(None)
