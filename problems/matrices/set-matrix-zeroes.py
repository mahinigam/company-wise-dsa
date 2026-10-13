"""Set Matrix Zeroes

Difficulty: Medium
Topic: matrices
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta, Adobe
Source: https://leetcode.com/problems/set-matrix-zeroes/

Problem summary: If any matrix cell is zero, set its entire row and column to zero in place.
Approach: Record zero rows and columns in sets, then zero cells in a second pass.
Complexity: O(rows×cols) time, O(rows+cols) space.
"""

def set_zeroes(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]: return
    rows = {r for r, row in enumerate(matrix) if 0 in row}
    cols = {c for c in range(len(matrix[0])) if any(matrix[r][c] == 0 for r in range(len(matrix)))}
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows or c in cols: matrix[r][c] = 0

grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_zeroes(grid)
assert grid == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
grid = [[0, 1]]; set_zeroes(grid); assert grid == [[0, 0]]
