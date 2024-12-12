from utilities import *
from rules import *
from board import *


def pencil_steps(board):
    """
    Goes through the rules that remove pencil marks.
    Will repeat previously done steps, so needs to
    be improved."""

    locked_candidates_square = Locked_Candidates_Square()

    for i in range(9):
        indices, num = locked_candidates_square.evaluate(i, board)
        if num:
            print(locked_candidates_square)
            print(f"{num} in square {i}")
            locked_candidates_square.do(i, board, indices, num)
            return True
        
        

def solve_step(board):
    """
    Solves a single step of a sudoku board.
    Prints what technique was used to solve the step
    The coordinates of the cell that was solved
    And returns True if a cell was solved, else False
    """
    
    # Check for Last Free Cell and Naked_Single
    rows, cols, sqrs = board.incomplete_houses()
    full_house = Full_House()
    naked_single = Naked_Single()
    hidden_single = Hidden_Single()

    
    for row in rows:
        
        # Full House
        number, index = full_house.evaluate(row[0])
        if number:
            print(full_house)
            print(f"{number} in : ({row[1]}, {index})")
            board.place_number((row[1], index), number)
            return True
        
        
        # Naked Single
        incomplete_cells = get_incomplete_cells_index(row[0])
        
        for cell in incomplete_cells:
            number = naked_single.evaluate((row[1], cell), board)
            if number:
                print(naked_single)
                print(f"{number} in : ({row[1]}, {cell})")
                board.place_number((row[1], cell), number)
                return True
        
            
        # Hidden Single
        for cell in incomplete_cells:
            number = hidden_single.evaluate((row[1], cell), board)
            if number:
                print(hidden_single)
                print(f"{number} in : ({row[1]}, {cell})")
                board.place_number((row[1], cell), number)
                return True
       
    for col in cols:
        # Full House
        
        number, index = full_house.evaluate(col[0])
        if number:
            print(full_house)
            print(f"{number} in : ({index}, {col[1]})")
            board.place_number((index, col[1]), number)
            return True
            
        
        # Naked_Single
        incomplete_cells = get_incomplete_cells_index(col[0])
        
        for cell in incomplete_cells:
            number = naked_single.evaluate((cell, col[1]), board)
            if number:
                print(naked_single)
                print(f"{number} in : ({cell}, {col[1]})")
                board.place_number((cell, col[1]), number)
                return True
                
            
        # Hidden Single
        for cell in incomplete_cells:
            number = hidden_single.evaluate((cell, col[1]), board)
            if number:
                print(hidden_single)
                print(f"{number} in : ({cell}, {col[1]})")
                board.place_number((cell, col[1]), number)
                return True
                
           
    for sqr in sqrs:
        # Last free cell
        number, index = full_house.evaluate(sqr[0])
        if number:
            coord = board.sqr_coord(sqr[1], index)
            print("Last free cell")
            print(f"{number} in : ({coord[0]}, {coord[1]})")
            board.place_number(coord, number)
            return True
        
        # Naked_Single
        incomplete_cells = get_incomplete_cells_index(sqr[0])
        
        for cell in incomplete_cells:
            coord = board.sqr_coord(sqr[1], cell)
            number = naked_single.evaluate(coord, board)
            if number:
                print("Naked Single")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                board.place_number(coord, number)
                return True
            
        # Hidden Single
        for cell in incomplete_cells:
            coord = board.sqr_coord(sqr[1], cell)
            number = hidden_single.evaluate(coord, board)
            if number:
                print("Hidden Single")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                board.place_number(coord, number)
                return True


  

    # If no technique was used, return the board
    print("No technique used")
    return False








