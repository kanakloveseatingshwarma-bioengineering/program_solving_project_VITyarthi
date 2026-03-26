"""
solver.py - Backtracking algorithm to solve Sudoku puzzles
"""

from sudoku.board import is_valid


def find_empty(board):
    """Finds the next empty cell (value = 0). Returns (row, col) or None."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve(board):
    """
    Solves the Sudoku board in-place using backtracking.
    Returns True if solved, False if unsolvable.
    """
    empty = find_empty(board)

    # Base case: no empty cells means puzzle is solved
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num       # Place the number

            if solve(board):            # Recurse
                return True

            board[row][col] = 0         # Backtrack

    return False  # Trigger backtracking in the caller


def count_solutions(board, limit=2):
    """
    Counts how many solutions a board has, up to 'limit'.
    Used to verify a puzzle has a unique solution.
    """
    empty = find_empty(board)
    if not empty:
        return 1

    row, col = empty
    count = 0

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            count += count_solutions(board, limit)
            board[row][col] = 0
            if count >= limit:
                return count

    return count


def has_unique_solution(board):
    """Returns True if the board has exactly one solution."""
    from sudoku.board import copy_board
    test_board = copy_board(board)
    return count_solutions(test_board) == 1
