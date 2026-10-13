"""Valid Sudoku

Difficulty: Medium
Topic: hashing
Preparation tags (not verified question attribution): Amazon, Uber, Adobe
Source: https://leetcode.com/problems/valid-sudoku/

Problem summary: Validate row, column, and 3×3-box uniqueness in a partially filled Sudoku board.
Approach: Track values seen for every row, column, and sub-box; ignore dots.
Complexity: O(1) time and space for a fixed 9×9 board.
"""

def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".": continue
            box = (r // 3) * 3 + c // 3
            if value in rows[r] or value in cols[c] or value in boxes[box]: return False
            rows[r].add(value); cols[c].add(value); boxes[box].add(value)
    return True

board = [["."] * 9 for _ in range(9)]
assert is_valid_sudoku(board)
board[0][0] = board[0][1] = "5"
assert not is_valid_sudoku(board)
