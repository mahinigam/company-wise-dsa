"""Maximum Depth of Binary Tree

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem summary: Compute the number of nodes on the longest root-to-leaf path.
Approach: Depth of a node is one plus the larger depth of its children.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def max_depth(root: TreeNode | None) -> int:
    return 0 if root is None else 1 + max(max_depth(root.left), max_depth(root.right))

assert max_depth(TreeNode(1, None, TreeNode(2))) == 2
assert max_depth(None) == 0
assert max_depth(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))) == 3
