"""Spiral Matrix

Difficulty: Medium
Topic: matrices
Preparation tags (not verified question attribution): Microsoft, Amazon, Google
Source: https://leetcode.com/problems/spiral-matrix/

Problem summary: Return matrix values in clockwise spiral order.
Approach: Move around four boundaries and shrink each boundary after traversing it.
Complexity: O(rows×cols) time and O(1) auxiliary space excluding output.
"""

def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]: return []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    out = []
    while top <= bottom and left <= right:
        out.extend(matrix[top][left:right + 1]); top += 1
        for r in range(top, bottom + 1): out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            out.extend(reversed(matrix[bottom][left:right + 1])); bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): out.append(matrix[r][left])
            left += 1
    return out

assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([]) == []
assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
