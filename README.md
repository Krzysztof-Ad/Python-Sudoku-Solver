# Sudoku Solver

This project is a Python-based Sudoku solver that uses a backtracking algorithm to solve any valid Sudoku puzzle. The solver is implemented in the `solving_algorithm.py` file and can be run from the command line.

## Algorithm

The Sudoku solver uses a backtracking algorithm to find the solution. Here's a breakdown of how it works:

1.  **Find an empty cell:** The algorithm scans the board to find the next empty cell (represented by a `0`).
2.  **Try a number:** It then tries to place a number from 1 to 9 in that empty cell.
3.  **Check for validity:** For each number, it checks if the move is valid according to Sudoku rules:
    *   The number is not already in the same row.
    *   The number is not already in the same column.
    *   The number is not already in the same 3x3 subgrid.
4.  **Recurse:** If the move is valid, the algorithm recursively calls itself to solve the rest of the puzzle.
5.  **Backtrack:** If the recursive call returns `False` (meaning it couldn't find a solution), the algorithm backtracks by resetting the cell to `0` and tries the next number.
6.  **Solution found:** If the algorithm fills all the empty cells, a solution has been found.

## How to Change the Input Board

To solve your own Sudoku puzzle, you need to modify the `sudoku_board` variable in the `solving_algorithm.py` file.

1.  **Open the file:** Open `solving_algorithm.py` in a text editor.
2.  **Locate the `sudoku_board` variable:** Find the following code block:
    ```python
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    ```
3.  **Edit the board:** Replace the numbers in the `sudoku_board` list with the numbers from your Sudoku puzzle. Use `0` to represent empty cells.

## How to Run

To run the Sudoku solver, simply run the `solving_algorithm.py` file from your terminal:

```bash
python solving_algorithm.py
```

