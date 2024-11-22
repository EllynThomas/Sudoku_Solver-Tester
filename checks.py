

def get_row(grid, row):
    # Returns row row from grid
    return grid[row]

def get_column(grid, col):
    # Returns column col from grid
    return [grid[i][col] for i in range(9)]

def get_square(grid, square):
    # Returns square number 'square' from grid
    # Squares are numbered 0-8 from top left to bottom right
    return [grid[(square // 3) * 3 + i][(square % 3) * 3 + j] for i in range(3) for j in range(3)]



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


