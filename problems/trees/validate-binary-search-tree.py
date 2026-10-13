"""Validate Binary Search Tree

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Google
Source: https://leetcode.com/problems/validate-binary-search-tree/

Problem summary: Check whether every node respects strict BST ordering.
Approach: Pass an exclusive lower and upper bound down the tree.
Complexity: O(n) time, O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_valid_bst(root: TreeNode | None) -> bool:
    def valid(node, low, high):
        if node is None: return True
        if not low < node.val < high: return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float("-inf"), float("inf"))

assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3)))
assert not is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
assert is_valid_bst(None)
