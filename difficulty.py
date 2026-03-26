"""
difficulty.py - Controls puzzle difficulty by removing cells from a solved board.
Ensures every generated puzzle has a unique solution.
"""

import random
from sudoku.board import copy_board
from sudoku.solver import has_unique_solution


# Number of cells to remove per difficulty level
DIFFICULTY_SETTINGS = {
    "easy":   35,
    "medium": 45,
    "hard":   55,
}


def make_puzzle(solved_board, difficulty="medium"):
    """
    Takes a fully solved board and removes cells to create a puzzle.
    Always ensures the resulting puzzle has a unique solution.
    """
    difficulty = difficulty.lower()
    if difficulty not in DIFFICULTY_SETTINGS:
        print(f"  Unknown difficulty '{difficulty}'. Defaulting to 'medium'.")
        difficulty = "medium"

    cells_to_remove = DIFFICULTY_SETTINGS[difficulty]
    puzzle = copy_board(solved_board)

    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)

    removed = 0
    for (row, col) in positions:
        if removed >= cells_to_remove:
            break

        backup = puzzle[row][col]
        puzzle[row][col] = 0

        if has_unique_solution(puzzle):
            removed += 1
        else:
            puzzle[row][col] = backup

    return puzzle


def get_difficulty_label(cells_removed):
    """Returns a human-readable difficulty label based on removed cell count."""
    if cells_removed <= 35:
        return "Easy"
    elif cells_removed <= 45:
        return "Medium"
    else:
        return "Hard"
