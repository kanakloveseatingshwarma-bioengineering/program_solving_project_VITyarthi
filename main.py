"""
main.py - Command-line interface for the Sudoku Generator & Solver

Run with:
    python main.py
"""

from sudoku.board import print_board, copy_board, count_empty_cells
from sudoku.generator import generate_solved_board
from sudoku.difficulty import make_puzzle, DIFFICULTY_SETTINGS
from sudoku.solver import solve


def print_banner():
    print("\n" + "=" * 45)
    print("        SUDOKU GENERATOR & SOLVER")
    print("=" * 45)


def print_menu():
    print("\n  What would you like to do?")
    print("  [1] Generate a new puzzle")
    print("  [2] Solve a puzzle (enter manually)")
    print("  [3] Exit")
    print()


def choose_difficulty():
    print("\n  Choose difficulty:")
    print("  [1] Easy   (~35 cells removed)")
    print("  [2] Medium (~45 cells removed)")
    print("  [3] Hard   (~55 cells removed)")
    choice = input("\n  Enter choice (1/2/3): ").strip()
    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    return mapping.get(choice, "medium")


def generate_flow():
    difficulty = choose_difficulty()

    print(f"\n  Generating a {difficulty.capitalize()} puzzle... ", end="", flush=True)
    solved_board = generate_solved_board()
    puzzle = make_puzzle(solved_board, difficulty)
    empty_count = count_empty_cells(puzzle)
    print("Done!")

    print(f"\n  Puzzle ({difficulty.capitalize()} — {empty_count} empty cells):")
    print_board(puzzle)

    while True:
        action = input("\n  [s] Show solution   [n] New puzzle   [m] Main menu: ").strip().lower()
        if action == "s":
            print("\n  Solution:")
            print_board(solved_board)
            break
        elif action == "n":
            generate_flow()
            return
        elif action == "m":
            return
        else:
            print("  Please enter s, n, or m.")


def manual_input_flow():
    print("\n  Enter your puzzle row by row.")
    print("  Use 0 for empty cells. Separate numbers with spaces.")
    print("  Example: 5 3 0 0 7 0 0 0 0\n")

    board = []
    for i in range(9):
        while True:
            try:
                raw = input(f"  Row {i + 1}: ").strip()
                nums = list(map(int, raw.split()))
                if len(nums) != 9 or not all(0 <= n <= 9 for n in nums):
                    raise ValueError
                board.append(nums)
                break
            except ValueError:
                print("  Invalid input. Enter exactly 9 numbers (0-9) separated by spaces.")

    print("\n  Your puzzle:")
    print_board(board)

    solve_copy = copy_board(board)
    print("\n  Solving... ", end="", flush=True)

    if solve(solve_copy):
        print("Solved!\n")
        print("  Solution:")
        print_board(solve_copy)
    else:
        print("No solution found.\n")
        print("  This puzzle has no valid solution. Please check your input.")


def main():
    print_banner()

    while True:
        print_menu()
        choice = input("  Enter choice (1/2/3): ").strip()

        if choice == "1":
            generate_flow()
        elif choice == "2":
            manual_input_flow()
        elif choice == "3":
            print("\n  Thanks for playing! Goodbye.\n")
            break
        else:
            print("\n  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
