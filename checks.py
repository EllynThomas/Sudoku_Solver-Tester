
### Functions for getting rows, columns, squares ###
def get_row(grid, row):
    # Returns row row from grid
    return grid[row]

def get_column(grid, col):
    # Returns column col from grid
    return [grid[i][col] for i in range(9)]

def get_square(grid, sqr):
    # Returns square number 'square' from grid
    # Squares are numbered 0-8 from top left to bottom right
    return [grid[(sqr // 3) * 3 + i][(sqr % 3) * 3 + j] for i in range(3) for j in range(3)]

def get_square_number(coord):
    # returns the square number for a given coordinate
    return 3 * (coord[0] // 3) + coord[1] // 3

def get_coord_from_square(sqr_number, index):
    # converts a square number and index to a coordinate
    return 3 * (sqr_number // 3) + index // 3, 3 * (sqr_number % 3) + index % 3

def get_square_index(coord):
    # returns the index of a cell in a square
    return 3 * (coord[0] % 3) + coord[1] % 3



### Functions for getting incomplete cells and sets ###

def get_empty_cells(grid):
    # Returns list of coordinates of all empty cells
    return [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]

def get_incomplete_cells_index(s):
    # Returns list of indexes of incomplete cells in a set
    return [i for i in range(9) if s[i] == 0]

def get_incomplete_sets(board):
    # Returns list of incomplete sets
    # returns a rows, columns, squares with its index

    rows = [(get_row(board, i), i) for i in range(9)]
    rows= [r for r in rows if 0 in r[0]]

    cols = [(get_column(board, i), i) for i in range(9)]
    cols = [c for c in cols if 0 in c[0]]

    sqrs = [(get_square(board, i), i) for i in range(9)]
    sqrs = [s for s in sqrs if 0 in s[0]]

    return rows, cols, sqrs








### Functions for checking validity ###

def check_complete_set(s):
    # Returns True if set contains ONLY 1-9 with no duplicates
    return set(s) == set(range(1, 10))

def check_partial_set(s):
    # Returns True if set contains 0s and no duplicates of 1-9 
    for i in range(8):
        if s[i] != 0 and s[i] in s[i+1:]:
            return False
    return True   

def check_valid_solution(grid, mods = None):
    # Checks if full grid is a valid solution
    # mods is list of additional constraints and their grids
    valid = True
    
    for i in range(9):
        if not check_complete_set(get_row(grid, i)):
            valid = False
        if not check_complete_set(get_column(grid, i)):
            valid = False
        if not check_complete_set(get_square(grid, i)):
            valid = False

        if not valid:
            return False
    
    if mods:
        print('Checking additional constraints')
        print('not implemented')
    
    return valid

def check_valid_partial(grid, mods = None):
    # Checks if partial grid is valid
    # mods is list of additional constraints and their grids
    valid = True
    
    for i in range(9):
        if not check_partial_set(get_row(grid, i)):
            valid = False
        if not check_partial_set(get_column(grid, i)):
            valid = False
        if not check_partial_set(get_square(grid, i)):
            valid = False

        if not valid:
            return False
    
    if mods:
        print('Checking additional constraints')
        print('not implemented')
    
    return valid

