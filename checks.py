from grid import *


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

    
    for i in range(9):
        if not check_complete_set(Sub_Grid(grid, SG_Type.ROW, i)()):
            return False
        if not check_complete_set(Sub_Grid(grid, SG_Type.COLUMN, i)()):
            return False
        if not check_complete_set(Sub_Grid(grid, SG_Type.SQUARE, i)()):
            return False
    
    if mods:
        print('Checking additional constraints')
        print('not implemented')
    
    return True

def check_valid_partial(grid, mods = None):
    # Checks if partial grid is valid
    # mods is list of additional constraints and their grids
    valid = True
    
    for i in range(9):
        if not check_partial_set(Sub_Grid(grid, SG_Type.ROW, i)()):
            valid = False
        if not check_partial_set(Sub_Grid(grid, SG_Type.COLUMN, i)()):
            valid = False
        if not check_partial_set(Sub_Grid(grid, SG_Type.SQUARE, i)()):
            valid = False

        if not valid:
            return False
    
    if mods:
        print('Checking additional constraints')
        print('not implemented')
    
    return valid

