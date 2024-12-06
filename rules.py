# Contains all techniques to fill a cell in a sudoku puzzle
from checks import *
from templates import HouseRule, CellRule, PencilHouseRule, PencilCellRule



### Utility Functions ###

def unfilled_numbers(house):
    # returns a set of all the numbers that are not 
    # filled in the house
    return set([i for i in range(1, 10) if i not in house])


def filled_numbers(house):
    # returns a set of all the numbers that are filled
    # in the house
    return set([i for i in range(1, 10) if i in house])


def pencil_cell(coord, grid):
    # Returns a set of possible numbers that can go in a cell
    row = unfilled_numbers(get_row(grid, coord[0]))
    col = unfilled_numbers(get_column(grid, coord[1]))
    square = unfilled_numbers(get_square(grid, get_square_number(coord)))

    return row & col & square





### House Techniques ###

class Full_House(HouseRule):
    # Full House Rule
    # Only one cell in a house is left to fill
    # returns number and index if true, else returns None
    def evaluate(self, house):
        unfilled = unfilled_numbers(house)

        if len(unfilled) == 1:
            return unfilled.pop(), house.index(0)
        return None, None

    def __str__(self):
        return "Full House Rule"
    






### Cell Techniques ###

class Naked_Single(CellRule):
    # Naked Single Rule
    # Only one number can go in a cell
    # returns number if true, else returns None
    def evaluate(self, coord, grid):
        candidates = pencil_cell(coord, grid)

        if len(candidates) == 1:
            return candidates.pop()
        return None

    def __str__(self):
        return "Naked Single Rule"


class Hidden_Single(CellRule):
    # Hidden Single Rule
    # Only one cell in a row, column or square can contain a number
    # returns number if true, else returns None
    def evaluate(self, coord, grid):
        candidates = pencil_cell(coord, grid)

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
                row_pencil.update(pencil_cell((coord[0], i), grid))
            if col[i] == 0 and i != coord[0]:
                col_pencil.update(pencil_cell((i, coord[1]), grid))
            if sqr[i] == 0 and i != sqr_i:
                sqr_pencil.update(pencil_cell(get_coord_from_square(sqr_num, i), grid))

            

        for candidate in candidates:
            if candidate not in row_pencil or candidate not in col_pencil or candidate not in sqr_pencil:
                return candidate
            

    def __str__(self):
        return "Hidden Single Rule"








