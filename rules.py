# Contains all techniques to fill a cell in a sudoku puzzle
from checks import *



### Utility Functions ###

def unfilled_numbers(s):
    # returns a list of all the numbers that are not 
    # filled in the set
    return [i for i in range(1, 10) if i not in s]

def get_square_number(coord):
    # returns the square number for a given coordinate
    return 3 * (coord[0] // 3) + coord[1] // 3

def pencil_marking(coord, grid):
    # Returns a list of possible numbers that can go in a cell
    # returns list of numbers
    row = unfilled_numbers(get_row(grid, coord[0]))
    col = unfilled_numbers(get_column(grid, coord[1]))
    square = unfilled_numbers(get_square(grid, coord[get_square_number(coord)]))

    return list(set(row) & set(col) & set(square))




### Set Techniques ###

def last_free_cell(s):
    # Only one cell in a set left to fill
    # returns number and index if true, else returns None
    unfilled = unfilled_numbers(s)

    if len(unfilled) == 1:
        return unfilled[0], s.index(0)
    return None

def unique_candidate(s, grid):
    # Only one cell in a row, column or square can contain a number
    # returns number and index if true, else returns None
    empty_cells = [i for i in range(9) if s[i] == 0]
    pencil_set = [pencil_marking((i, s.index(0)), grid) for i in empty_cells]

    for i in range(1, 10):
        if sum([i in p for p in pencil_set]) == 1:
            return i, empty_cells[pencil_set.index([i])]
    return None


### Cell Techniques ###

def sole_candidate(coord, grid):
    # Only one number can go in a cell
    # returns number if true, else returns None
    candidates = pencil_marking(coord, grid)

    if len(candidates) == 1:
        return candidates[0]
    return None












