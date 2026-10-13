"""Path Sum

Difficulty: Easy
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Target
Source: https://leetcode.com/problems/path-sum/

Problem summary: Check whether any root-to-leaf path sums to target.
Approach: Subtract each visited node value and succeed only at a leaf with remainder zero.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if root is None: return False
    if root.left is None and root.right is None: return root.val == target_sum
    remainder = target_sum - root.val
    return has_path_sum(root.left, remainder) or has_path_sum(root.right, remainder)

root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
assert has_path_sum(root, 22)
assert not has_path_sum(root, 28)
assert not has_path_sum(None, 0)
