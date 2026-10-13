"""Sum of Left Leaves

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/sum-of-left-leaves/

Problem summary: Sum values of leaf nodes that are left children.
Approach: DFS passes a flag indicating whether a node is its parent's left child.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def sum_of_left_leaves(root: TreeNode | None) -> int:
    def visit(node, is_left):
        if node is None: return 0
        if node.left is None and node.right is None: return node.val if is_left else 0
        return visit(node.left, True) + visit(node.right, False)
    return visit(root, False)

assert sum_of_left_leaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 24
assert sum_of_left_leaves(None) == 0
