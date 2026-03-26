# program_solving_project_VITyarthi
Sudoku Generator and Solver built in Python that creates puzzles with varying difficulty levels and guarantees a unique solution. Uses randomized generation and backtracking to solve puzzles. Users can also input and solve custom Sudoku boards via a command-line interface.
# Overview of the Project
This project is a Sudoku Generator and Solver implemented in Python. It allows users to generate Sudoku puzzles of varying difficulty levels and solve puzzles either automatically or through manual input.

The system ensures that every generated puzzle has a valid and unique solution. This is achieved by combining randomized board generation with a backtracking-based solving algorithm.

The program is structured in a modular way, where different components handle generation, solving, and difficulty adjustment. The main interface is a command-line program defined in main.py, which connects all modules and manages user interaction.
# Features
1. Generate Sudoku puzzles with three difficulty levels: Easy, Medium, and Hard
2. Ensure every generated puzzle has a unique solution
3. Solve Sudoku puzzles using a backtracking algorithm
4. Allow users to input their own puzzles for solving
5. Randomized puzzle generation for variety
6. Modular code structure for clarity and maintainability
7. Input validation for user-entered puzzles
# Technologies/Tools used
1. Python (core programming language)
2. Backtracking algorithm for solving Sudoku
3. Random module for generating different board configurations
4. Modular programming using multiple Python files

No external libraries are required to run this project.
# Steps to Install and Run the Project
Step 1: Clone the repository

git clone <your-repository-link>
cd sudoku-project

Step 2: Ensure the project structure

sudoku-project/
│
├── sudoku/
│ ├── board.py
│ ├── generator.py
│ ├── solver.py
│ ├── difficulty.py
│ └── init.py
│
├── main.py

Step 3: Run the program

python main.py

Step 4: Follow the menu options displayed in the terminal
# Instructions for Testing
Test Case 1: Generate a Puzzle

1. Select option 1 from the menu
2. Choose a difficulty level
3. Verify that the puzzle is displayed correctly
4. Check that empty cells are present
5. Use the option to display the solution and verify correctness

Test Case 2: Solve a Custom Puzzle

1. Select option 2 from the menu
2. Enter a valid Sudoku puzzle row by row using 0 for empty cells
3. Verify that the program correctly solves the puzzle

Test Case 3: Invalid Input Handling

1. Enter incorrect input such as letters or fewer than 9 numbers
2. Verify that the program displays an error message and prompts again

Test Case 4: Unsolvable Puzzle

1. Enter a puzzle with no valid solution
2. Verify that the program outputs a “No solution found” message

Test Case 5: Difficulty Verification

1. Generate puzzles of different difficulty levels
2. Observe that the number of empty cells increases from Easy to Hard
