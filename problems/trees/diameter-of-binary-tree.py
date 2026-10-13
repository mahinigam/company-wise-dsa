"""Diameter of Binary Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/diameter-of-binary-tree/

Problem summary: Compute the maximum number of edges on a path between any two nodes.
Approach: Compute subtree heights and update the best diameter through each node.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def diameter_of_binary_tree(root: TreeNode | None) -> int:
    best = 0
    def height(node):
        nonlocal best
        if node is None: return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)
    height(root)
    return best

assert diameter_of_binary_tree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
assert diameter_of_binary_tree(TreeNode(1)) == 0
