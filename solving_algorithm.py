def print_grid(grid):
    print("\n+-------+-------+-------+")
    for row in range(len(grid)):
        print("|", end=" ")
        for col in range(len(grid[0])):
            print(grid[row][col] if grid[row][col] != 0 else ".", end=" ")
            if (col + 1) % 3 == 0:
                print("|", end=" ")
        print()
        if (row + 1) % 3 == 0:
            print("+-------+-------+-------+")

def validation(grid, position, value):
    row = position[0]
    col = position[1]

    #row validation
    for j in range(0, len(grid[0])):
        if grid[row][j] == value and j != col:
            return False

    #column validation
    for i in range(0, len(grid)):
        if grid[i][col] == value and i != row:
            return False

    #3x3 box validation
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range (box_start_row, box_start_row + 3):
        for j in range (box_start_col, box_start_col + 3):
            if grid[i][j] == value and (i != row or j != col):
                return False

    return True

def find_empty_cell(grid):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)
    return None

def solve_sudoku(grid):
    position = find_empty_cell(grid)
    if position is None:
        return True
    else:
        for num in range(1,10):
            if validation(grid, position, num):
                grid[position[0]][position[1]] = num
                if solve_sudoku(grid):
                    return True

    grid[position[0]][position[1]] = 0
    return False

if __name__ == "__main__":

    print("--- Welcome to the Sudoku solver! ---")

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

    print("\n--- Board Before Solving ---")
    print_grid(sudoku_board)

    print("\n--- Starting Sudoku Solver... ---")

    if solve_sudoku(sudoku_board):
        print("\n--- Success! Sudoku Solved ---")
        print_grid(sudoku_board)
    else:
        print("\n--- Error! Sudoku Is Not Solvable ---")