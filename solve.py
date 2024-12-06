from checks import *
from rules import *

def print_board(board):
    """
    Prints a sudoku board
    """
    print(''.join(['-' for i in range(25)]))
    for i in range(9):
        print('|', end = '')
        for j in range(9):
            print(f' {board[i][j]}', end = '')
            if j % 3 == 2:
                print(' |', end = '')
        print()
        if i % 3 == 2:
            print(''.join(['-' for i in range(25)]))
    
    print()

def place_number(board, coord, number):
    """
    Places a number in a cell on the board
    """
    if board[coord[0]][coord[1]] != 0:
        print(f"Cell ({coord[0]}, {coord[1]}) already filled")
        return board
    
    board[coord[0]][coord[1]] = number
    return board




def solve_step(board):
    """
    Solves a single step of a sudoku board.
    Prints what technique was used to solve the step
    The coordinates of the cell that was solved
    And returns the new board
    """
    '''
    # Check for Naked_Single
    board, solved = sole_candidate(board)
    if solved:
        print("Naked_Single")
        print(f"Solved cell: {solved}")
        return board
    '''
    # Check for Last Free Cell and Naked_Single
    rows, cols, sqrs = get_incomplete_sets(board)
    full_house = Full_House()
    naked_single = Naked_Single()
    hidden_single = Hidden_Single()
    
    for row in rows:
        
        # Full House
        number, index = full_house.evaluate(row[0])
        if number:
            print("Full House")
            print(f"{number} in : ({row[1]}, {index})")
            return place_number(board, (row[1], index), number)
        
        
        # Naked Single
        incomplete_cells = get_incomplete_cells_index(row[0])
        
        for cell in incomplete_cells:
            number = naked_single.evaluate((row[1], cell), board)
            if number:
                print("Naked_Single")
                print(f"{number} in : ({row[1]}, {cell})")
                return place_number(board, (row[1], cell), number)
        
            
        # Hidden Single
        for cell in incomplete_cells:
            number = hidden_single.evaluate((row[1], cell), board)
            if number:
                print("Hidden Single")
                print(f"{number} in : ({row[1]}, {cell})")
                return place_number(board, (row[1], cell), number)
       
    for col in cols:
        # Last free cell
        
        number, index = full_house.evaluate(col[0])
        if number:
            print("Last free cell")
            print(f"{number} in : ({index}, {col[1]})")
            return place_number(board, (index, col[1]), number)
        
        # Naked_Single
        incomplete_cells = get_incomplete_cells_index(col[0])
        
        for cell in incomplete_cells:
            number = naked_single.evaluate((cell, col[1]), board)
            if number:
                print("Naked_Single")
                print(f"{number} in : ({cell}, {col[1]})")
                return place_number(board, (cell, col[1]), number)
            
        # Hidden Single
        for cell in incomplete_cells:
            number = hidden_single.evaluate((cell, col[1]), board)
            if number:
                print("Hidden Single")
                print(f"{number} in : ({cell}, {col[1]})")
                return place_number(board, (cell, col[1]), number)
     
            
    for sqr in sqrs:
        # Last free cell
        
        number, index = full_house.evaluate(sqr[0])
        if number:
            coord = get_coord_from_square(sqr[1], index)
            print("Last free cell")
            print(f"{number} in : ({coord[0]}, {coord[1]})")
            return place_number(board, coord, number)
        
        # Naked_Single
        incomplete_cells = get_incomplete_cells_index(sqr[0])
        
        for cell in incomplete_cells:
            coord = get_coord_from_square(sqr[1], cell)
            number = naked_single.evaluate(coord, board)
            if number:
                print("Naked_Single")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                return place_number(board, coord, number)
            
        # Hidden Single
        for cell in incomplete_cells:
            coord = get_coord_from_square(sqr[1], cell)
            number = hidden_single.evaluate(coord, board)
            if number:
                print("Hidden Single")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                return place_number(board, coord, number)



    # If no technique was used, return the board
    print("No technique used")
    return board








