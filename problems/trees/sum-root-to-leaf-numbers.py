"""Sum Root to Leaf Numbers

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/sum-root-to-leaf-numbers/

Problem summary: Sum numbers formed by concatenating digits along root-to-leaf paths.
Approach: Carry the current numeric prefix downward and add it at leaves.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def sum_numbers(root: TreeNode | None) -> int:
    def visit(node, prefix):
        if node is None: return 0
        value = prefix * 10 + node.val
        if node.left is None and node.right is None: return value
        return visit(node.left, value) + visit(node.right, value)
    return visit(root, 0)

assert sum_numbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
assert sum_numbers(None) == 0
