"""
generator.py - Generates valid, fully solved Sudoku boards
"""

import random
from sudoku.board import create_empty_board, is_valid
from sudoku.solver import solve


def generate_solved_board():
    """
    Generates a completely solved, valid Sudoku board.
    """
    board = create_empty_board()

    # Fill the three diagonal boxes independently (safe — no conflicts possible)
    for box in range(3):
        fill_box(board, box * 3, box * 3)

    # Use the solver (with randomised fill) to complete the rest
    solve_random(board)

    return board


def fill_box(board, start_row, start_col):
    """Fills a 3x3 box with random numbers 1-9."""
    nums = list(range(1, 10))
    random.shuffle(nums)
    idx = 0
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            board[i][j] = nums[idx]
            idx += 1


def solve_random(board):
    """
    Like the standard solver, but shuffles numbers 1-9 before trying them.
    This produces a different valid solution each time.
    """
    from sudoku.solver import find_empty

    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)

    for num in nums:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_random(board):
                return True
            board[row][col] = 0

    return False
