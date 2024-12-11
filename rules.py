# Contains all techniques to fill a cell in a sudoku puzzle
from utilities import *
from templates import HouseRule, CellRule, PencilHouseRule, PencilCellRule






### House Techniques ###

class Full_House(HouseRule):
    # Only one cell in a house is left to fill
    # returns number and index if true, else returns None
    def evaluate(self, house):
        unfilled = unfilled_numbers(house)

        if len(unfilled) == 1:
            return unfilled.pop(), house.index(0)
        return None, None

    def __str__(self):
        return "Full House Rule"
    
class Locked_Candidates_Square(PencilHouseRule):
    # If a number is only possible in a row or column in a square
    # then it can be removed from the rest of square
    # returns list of indices and number if true, else returns None
    def evaluate(self, square_number, board):

        row_candidates = []
        col_candidates = []
        
        for i in range(3):
            # Get the coordinates of each row/column in the square
            row_coords = [board.sqr_coord(square_number, i * 3 + j) for j in range(3)]
            col_coords = [board.sqr_coord(square_number, i + j * 3) for j in range(3)]

            # Get the pencil marks for each row/column
            row_candidates.append(set(board.pencil_cell(coord) for coord in row_coords))
            col_candidates.append(set(board.pencil_cell(coord) for coord in col_coords))


        # Check if a number is only possible in one row or column
        for i in range(3):
            for candidate in row_candidates[i]:
                if candidate not in row_candidates[(i + 1) % 3] and candidate not in row_candidates[(i + 2) % 3]:
                    return [i * 3 + j for j in range(3)], candidate.pop()
                if candidate not in col_candidates[(i + 1) % 3] and candidate not in col_candidates[(i + 2) % 3]:
                    return [i + j * 3 for j in range(3)], candidate.pop()

        return None, None
    
    def __str__(self):
        return "Locked Candidates Rule"

    def do(self, square_number, board, indices, number):
        # Remove the number from the rest of the square
        board_indices = []
        for i in range(9): 
            if i not in indices: board_indices.append(i)


        for index in board_indices:
            coord = board.sqr_coord(square_number, index)
            board.remove_pencil(coord, number)        

        
class Locked_Candidates_Line(PencilHouseRule):
    # If a number is only possible in one square in a row or column
    # then it can be removed from the rest of the row/column
    # returns list of indexes and number if true, else returns None

    def evaluate(self, house, board):
        pass
        







### Cell Techniques ###

class Naked_Single(CellRule):
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








