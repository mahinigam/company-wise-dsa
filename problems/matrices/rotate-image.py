"""Rotate Image

Difficulty: Medium
Topic: matrices
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/rotate-image/

Problem summary: Rotate an n×n matrix 90 degrees clockwise in place.
Approach: Transpose the matrix, then reverse each row.
Complexity: O(n²) time and O(1) extra space.
"""

def rotate_image(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix: row.reverse()

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_image(grid)
assert grid == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
grid = [[1]]; rotate_image(grid); assert grid == [[1]]
