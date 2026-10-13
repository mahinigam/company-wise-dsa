"""Lowest Common Ancestor of a BST

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem summary: Find the lowest node that has both target nodes as descendants.
Approach: Use BST ordering: move left or right while both targets fall on the same side.
Complexity: O(h) time and O(1) extra space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def lowest_common_ancestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    while root:
        if p.val < root.val and q.val < root.val: root = root.left
        elif p.val > root.val and q.val > root.val: root = root.right
        else: return root
    return None

root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4)), TreeNode(8, TreeNode(7), TreeNode(9)))
assert lowest_common_ancestor(root, root.left, root.right).val == 6
assert lowest_common_ancestor(root, root.left, root.left.right).val == 2
