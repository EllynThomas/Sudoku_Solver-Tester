# Contains all techniques to fill a cell in a sudoku puzzle
from utilities import *
from templates import HouseRule, CellRule, PencilHouseRule, PencilCellRule






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
    def evaluate(self, coord, board):
        candidates = board.pencil_cell(coord)
        if len(candidates) == 1:
            return candidates.pop()
        return None

    def __str__(self):
        return "Naked Single Rule"


class Hidden_Single(CellRule):
    # Hidden Single Rule
    # Only one cell in a row, column or square can contain a number
    # returns number if true, else returns None
    def evaluate(self, coord, board):
        candidates = board.pencil_cell(coord)

        row, col, sqr = board.houses(coord)

        row_pencil = set()
        col_pencil = set()
        sqr_pencil = set()

        sqr_num = board.sqr_number(coord)
        sqr_index = board.sqr_index(coord)

        for i in range(9):
            if row[i] == 0 and i != coord[1]:
                row_pencil.update(board.pencil_grid[coord[0]][i])
            if col[i] == 0 and i != coord[0]:
                col_pencil.update(board.pencil_grid[i][coord[1]])
            if sqr[i] == 0 and i != sqr_index:
                sqr_pencil.update(board.pencil_grid[board.sqr_coord(sqr_num, i)[0]][board.sqr_coord(sqr_num, i)[1]])
           

        for candidate in candidates:
            if candidate not in row_pencil or candidate not in col_pencil or candidate not in sqr_pencil:
                return candidate
            

    def __str__(self):
        return "Hidden Single Rule"








