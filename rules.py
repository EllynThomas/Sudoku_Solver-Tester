# Contains all techniques to fill a cell in a sudoku puzzle
from checks import *



### Utility Functions ###

def unfilled_numbers(s):
    # returns a list of all the numbers that are not 
    # filled in the set
    return [i for i in range(1, 10) if i not in s]


def pencil_marking(coord, grid):
    # Returns a list of possible numbers that can go in a cell
    # returns list of numbers
    row = unfilled_numbers(get_row(grid, coord[0]))
    col = unfilled_numbers(get_column(grid, coord[1]))
    square = unfilled_numbers(get_square(grid, get_square_number(coord)))

    return list(set(row) & set(col) & set(square))




### Set Techniques ###

def lfc_rule(s):
    # Last Free Cell Rule
    # Only one cell in a set left to fill
    # returns number and index if true, else returns None
    unfilled = unfilled_numbers(s)

    if len(unfilled) == 1:
        return unfilled[0], s.index(0)
    return None, None




### Cell Techniques ###

def sc_rule(coord, grid):
    # Sole Candidate Rule
    # Only one number can go in a cell
    # returns number if true, else returns None
    candidates = pencil_marking(coord, grid)

    if len(candidates) == 1:
        return candidates[0]
    return None



#### Change to cell technique
def uc_rule(coord, grid):
    # Unique Candidate Rule
    # Only one cell in a row, column or square can contain a number
    # returns number and index if true, else returns None
    candidates = pencil_marking(coord, grid)

    row = get_row(grid, coord[0])
    col = get_column(grid, coord[1])
    sqr = get_square(grid, get_square_number(coord))

    row_pencil = set()
    col_pencil = set()
    sqr_pencil = set()

    sqr_num = get_square_number(coord)
    sqr_i = get_square_index(coord)
    

    for i in range(9):
        if row[i] == 0 and i != coord[1]:
            row_pencil.update(pencil_marking((coord[0], i), grid))
        if col[i] == 0 and i != coord[0]:
            col_pencil.update(pencil_marking((i, coord[1]), grid))
        if sqr[i] == 0 and i != sqr_i:
            sqr_pencil.update(pencil_marking(get_coord_from_square(sqr_num, i), grid))

        

    for candidate in candidates:
        if candidate not in row_pencil or candidate not in col_pencil or candidate not in sqr_pencil:
            return candidate
        









