
# This file contains utility functions for the sudoku solver

def get_incomplete_cells_index(house):
    # Returns list of indexes of incomplete cells in a set
    return [i for i in range(9) if house[i] == 0]

def unfilled_numbers(house):
    # returns a set of all the numbers that are not 
    # filled in the house
    return set([i for i in range(1, 10) if i not in house])

def filled_numbers(house):
    # returns a set of all the numbers that are filled
    # in the house
    return set([i for i in range(1, 10) if i in house])






''' Functions for checking validity '''

def check_complete_set(s):
    # Returns True if set contains ONLY 1-9 with no duplicates
    return set(s) == set(range(1, 10))

def check_partial_set(s):
    # Returns True if set contains 0s and no duplicates of 1-9 
    for i in range(8):
        if s[i] != 0 and s[i] in s[i+1:]:
            return False
    return True   




