"""
board.py - Core Sudoku grid logic, validation, and display
"""


def create_empty_board():
    """Returns a 9x9 grid filled with zeros (empty cells)."""
    return [[0] * 9 for _ in range(9)]


def is_valid(board, row, col, num):
    """
    Check if placing 'num' at board[row][col] is valid.
    Checks the row, column, and 3x3 box.
    """
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row = 3 * (row // 3)
    box_col = 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


def copy_board(board):
    """Returns a deep copy of the board."""
    return [row[:] for row in board]


def print_board(board):
    """Prints the Sudoku board in a clean, readable format."""
    print("\n  +" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+")
    for i in range(9):
        row_str = "  | "
        for j in range(9):
            val = board[i][j]
            row_str += (str(val) if val != 0 else ".") + " "
            if (j + 1) % 3 == 0:
                row_str += "| "
        print(row_str)
        if (i + 1) % 3 == 0:
            print("  +" + "-" * 7 + "+" + "-" * 7 + "+" + "-" * 7 + "+")


def count_empty_cells(board):
    """Returns the number of empty cells (zeros) in the board."""
    return sum(row.count(0) for row in board)


def is_complete(board):
    """Returns True if the board has no empty cells."""
    return count_empty_cells(board) == 0
