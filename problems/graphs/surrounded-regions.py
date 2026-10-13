"""Surrounded Regions

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/surrounded-regions/

Problem summary: Capture 'O' regions not connected to the board boundary by converting them to 'X'.
Approach: Flood-fill boundary-connected O cells as safe, then flip remaining O cells.
Complexity: O(rows×cols) time and O(rows×cols) space.
"""

def solve_surrounded(board: list[list[str]]) -> None:
    if not board or not board[0]: return
    rows, cols = len(board), len(board[0]); stack = []
    for r in range(rows):
        for c in (0, cols - 1):
            if board[r][c] == "O": stack.append((r, c))
    for c in range(cols):
        for r in (0, rows - 1):
            if board[r][c] == "O": stack.append((r, c))
    while stack:
        r, c = stack.pop()
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != "O": continue
        board[r][c] = "#"
        stack.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O": board[r][c] = "X"
            elif board[r][c] == "#": board[r][c] = "O"

grid = [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")]
solve_surrounded(grid)
assert ["".join(row) for row in grid] == ["XXXX", "XXXX", "XXXX", "XOXX"]
