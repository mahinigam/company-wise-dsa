"""Binary Tree Tilt

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/binary-tree-tilt/

Problem summary: Sum each node's tilt, defined as the absolute difference between left and right subtree sums.
Approach: Postorder DFS returns subtree sums and accumulates each node's tilt.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def find_tilt(root: TreeNode | None) -> int:
    total_tilt = 0
    def subtree_sum(node):
        nonlocal total_tilt
        if node is None: return 0
        left, right = subtree_sum(node.left), subtree_sum(node.right)
        total_tilt += abs(left - right)
        return node.val + left + right
    subtree_sum(root)
    return total_tilt

assert find_tilt(TreeNode(1, TreeNode(2), TreeNode(3))) == 1
assert find_tilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))) == 15
assert find_tilt(None) == 0
