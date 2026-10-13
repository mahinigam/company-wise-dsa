"""Binary Tree Maximum Path Sum

Difficulty: Hard
Topic: trees
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Problem summary: Find the maximum sum of a non-empty path in a binary tree.
Approach: Postorder DFS returns the best one-sided gain while updating a global best with both child gains.
Complexity: O(n) time, O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def max_path_sum(root: TreeNode | None) -> int:
    if root is None: raise ValueError("tree must be non-empty")
    best = float("-inf")
    def gain(node):
        nonlocal best
        if node is None: return 0
        left, right = max(0, gain(node.left)), max(0, gain(node.right))
        best = max(best, node.val + left + right)
        return node.val + max(left, right)
    gain(root)
    return int(best)

assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
assert max_path_sum(TreeNode(-3)) == -3
