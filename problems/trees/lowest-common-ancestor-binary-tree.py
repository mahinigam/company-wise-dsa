"""Lowest Common Ancestor of a Binary Tree

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Problem summary: Find the lowest node that is an ancestor of both target nodes in a general binary tree.
Approach: Return a target when found; if left and right subtrees both return non-empty nodes, current node is the LCA.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None or root is p or root is q: return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right: return root
    return left or right

p, q = TreeNode(5), TreeNode(1)
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1, TreeNode(0), TreeNode(8)))
p, q = root.left, root.right
assert lowest_common_ancestor(root, p, q) is root
assert lowest_common_ancestor(root, root.left, root.left.right).val == 5
