"""Kth Smallest Element in a BST

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Problem summary: Return the kth smallest value in a binary search tree.
Approach: Inorder traversal visits BST values in sorted order; stop after k visits.
Complexity: O(h+k) time in the usual traversal, O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def kth_smallest(root: TreeNode | None, k: int) -> int:
    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node); node = node.left
        node = stack.pop()
        k -= 1
        if k == 0: return node.val
        node = node.right
    raise ValueError("k exceeds the number of nodes")

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
assert kth_smallest(root, 1) == 1
assert kth_smallest(root, 3) == 3
