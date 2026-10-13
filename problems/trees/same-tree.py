"""Same Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Target
Source: https://leetcode.com/problems/same-tree/

Problem summary: Check if two binary trees have identical structure and values.
Approach: Recursively compare the current values and corresponding subtrees.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None or q is None: return p is q
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

assert is_same_tree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
assert not is_same_tree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
assert is_same_tree(None, None)
