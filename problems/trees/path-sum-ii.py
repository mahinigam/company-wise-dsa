"""Path Sum II

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/path-sum-ii/

Problem summary: Return every root-to-leaf path whose values sum to target.
Approach: DFS maintains a current path and remaining target sum, backtracking after each branch.
Complexity: O(n·h) output-sensitive time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def path_sum_paths(root: TreeNode | None, target_sum: int) -> list[list[int]]:
    out = []
    def visit(node, remaining, path):
        if node is None: return
        path.append(node.val); remaining -= node.val
        if node.left is None and node.right is None and remaining == 0: out.append(path[:])
        else:
            visit(node.left, remaining, path); visit(node.right, remaining, path)
        path.pop()
    visit(root, target_sum, [])
    return out

root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
assert {tuple(p) for p in path_sum_paths(root, 22)} == {(5,4,11,2), (5,8,4,5)}
