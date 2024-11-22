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
    # Check for sole candidate
    board, solved = sole_candidate(board)
    if solved:
        print("Sole candidate")
        print(f"Solved cell: {solved}")
        return board
    '''
    # Check for Last Free Cell and Sole Candidate
    rows, cols, sqrs = get_incomplete_sets(board)
    
    for row in rows:
        
        # Last free cell
        number, index = lfc_rule(row[0])
        if number:
            print("Last free cell")
            print(f"{number} in : ({row[1]}, {index})")
            return place_number(board, (row[1], index), number)
        
        
        # Sole candidate
        incomplete_cells = get_incomplete_cells_index(row[0])
        
        for cell in incomplete_cells:
            number = sc_rule((row[1], cell), board)
            if number:
                print("Sole candidate")
                print(f"{number} in : ({row[1]}, {cell})")
                return place_number(board, (row[1], cell), number)
        
            
        # Unique candidate
        for cell in incomplete_cells:
            number = uc_rule((row[1], cell), board)
            if number:
                print("Unique candidate")
                print(f"{number} in : ({row[1]}, {cell})")
                return place_number(board, (row[1], cell), number)
       
    for col in cols:
        # Last free cell
        
        number, index = lfc_rule(col[0])
        if number:
            print("Last free cell")
            print(f"{number} in : ({index}, {col[1]})")
            return place_number(board, (index, col[1]), number)
        
        # Sole candidate
        incomplete_cells = get_incomplete_cells_index(col[0])
        
        for cell in incomplete_cells:
            number = sc_rule((cell, col[1]), board)
            if number:
                print("Sole candidate")
                print(f"{number} in : ({cell}, {col[1]})")
                return place_number(board, (cell, col[1]), number)
            
        # Unique candidate
        for cell in incomplete_cells:
            number = uc_rule((cell, col[1]), board)
            if number:
                print("Unique candidate")
                print(f"{number} in : ({cell}, {col[1]})")
                return place_number(board, (cell, col[1]), number)
     
            
    for sqr in sqrs:
        # Last free cell
        
        number, index = lfc_rule(sqr[0])
        if number:
            coord = get_coord_from_square(sqr[1], index)
            print("Last free cell")
            print(f"{number} in : ({coord[0]}, {coord[1]})")
            return place_number(board, coord, number)
        
        # Sole candidate
        incomplete_cells = get_incomplete_cells_index(sqr[0])
        
        for cell in incomplete_cells:
            coord = get_coord_from_square(sqr[1], cell)
            number = sc_rule(coord, board)
            if number:
                print("Sole candidate")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                return place_number(board, coord, number)
            
        # Unique candidate
        for cell in incomplete_cells:
            coord = get_coord_from_square(sqr[1], cell)
            number = uc_rule(coord, board)
            if number:
                print("Unique candidate")
                print(f"{number} in : ({coord[0]}, {coord[1]})")
                return place_number(board, coord, number)



    # If no technique was used, return the board
    print("No technique used")
    return board






# Sudoku boards

def select_board(board):
    """
    Selects a board from the list of sample boards
    """

    # Very easy
    
    if board == 've1':
        # Only requires last free cell
        # 5 steps
        return     [[0, 3, 7, 1, 5, 2, 9, 0, 8],
                    [1, 2, 9, 8, 4, 7, 5, 3, 6],
                    [5, 0, 8, 6, 3, 9, 7, 2, 1],
                    [9, 7, 3, 2, 1, 5, 8, 6, 4],
                    [4, 1, 5, 7, 6, 0, 2, 9, 3],
                    [8, 6, 2, 4, 9, 3, 1, 0, 7],
                    [3, 9, 1, 5, 8, 6, 4, 7, 2],
                    [2, 5, 4, 3, 7, 1, 6, 8, 0],
                    [7, 8, 0, 9, 2, 4, 3, 1, 5]]
    

    # Easy
    
    elif board == 'e1':
        # Also requires sole candidate
        # 45 steps
        return     [[0, 0, 7, 0, 0, 2, 0, 4, 8],
                    [1, 2, 9, 8, 0, 0, 0, 0, 0],
                    [0, 0, 8, 6, 3, 0, 7, 0, 1],
                    [9, 7, 0, 2, 1, 0, 0, 0, 0],
                    [4, 1, 0, 0, 0, 8, 0, 0, 3],
                    [0, 0, 0, 0, 0, 3, 1, 5, 7],
                    [3, 0, 0, 0, 8, 6, 4, 0, 0],
                    [0, 5, 4, 0, 7, 0, 6, 0, 0],
                    [7, 8, 0, 0, 0, 4, 3, 1, 0]]
    

    elif board == 'h1':
        # Also requires unique candidate, + more
        # 60 steps
        return [[0, 6, 0, 3, 0, 0, 0, 0, 0],
                [9, 0, 0, 0, 6, 2, 0, 5, 0],
                [0, 0, 0, 8, 7, 0, 0, 0, 2],
                [1, 0, 9, 5, 0, 0, 0, 0, 7],
                [0, 4, 7, 0, 0, 0, 0, 0, 0],
                [0, 3, 0, 0, 0, 0, 2, 9, 0],
                [0, 0, 0, 0, 0, 3, 5, 0, 4],
                [0, 7, 0, 0, 0, 4, 0, 6, 0],
                [0, 0, 1, 6, 0, 0, 8, 0, 0]]
    else:
        return None

def select_board_solution(board):
    """
    Selects the solution to a board from the list of boards
    """
    if board == 've1':
        return  [[6, 3, 7, 1, 5, 2, 9, 4, 8],
                 [1, 2, 9, 8, 4, 7, 5, 3, 6],
                 [5, 4, 8, 6, 3, 9, 7, 2, 1],
                 [9, 7, 3, 2, 1, 5, 8, 6, 4],
                 [4, 1, 5, 7, 6, 8, 2, 9, 3],
                 [8, 6, 2, 4, 9, 3, 1, 5, 7],
                 [3, 9, 1, 5, 8, 6, 4, 7, 2],
                 [2, 5, 4, 3, 7, 1, 6, 8, 9],
                 [7, 8, 6, 9, 2, 4, 3, 1, 5]]
    
    elif board == 'e1':
        return     [[6, 3, 7, 1, 5, 2, 9, 4, 8],
                    [1, 2, 9, 8, 4, 7, 5, 3, 6],
                    [5, 4, 8, 6, 3, 9, 7, 2, 1],
                    [9, 7, 3, 2, 1, 5, 8, 6, 4],
                    [4, 1, 5, 7, 6, 8, 2, 9, 3],
                    [8, 6, 2, 4, 9, 3, 1, 5, 7],
                    [3, 9, 1, 5, 8, 6, 4, 7, 2],
                    [2, 5, 4, 3, 7, 1, 6, 8, 9],
                    [7, 8, 6, 9, 2, 4, 3, 1, 5]]
    
    elif board == 'h1':
        return [[7, 6, 2, 3, 1, 5, 9, 4, 8],
                [9, 8, 3, 4, 6, 2, 7, 5, 1],
                [5, 1, 4, 8, 7, 9, 6, 3, 2],
                [1, 2, 9, 5, 3, 6, 4, 8, 7],
                [6, 4, 7, 9, 2, 8, 3, 1, 5],
                [8, 3, 5, 7, 4, 1, 2, 9, 6],
                [2, 9, 6, 1, 8, 3, 5, 7, 4],
                [3, 7, 8, 2, 5, 4, 1, 6, 9],
                [4, 5, 1, 6, 9, 7, 8, 2, 3]]
    else:
        return None




def tests():
    """
    Runs tests for the solve_step function
    """

    # Very easy 1
    board = select_board('h1')
    print_board(board)

    for i in range(10):
        print('Step', i+1)
        board = solve_step(board)
        print(' ')

        # print_board(board)
        if check_valid_solution(board):
            print('Solved')
            break
    print_board(board)
    print('Matches solution? ' +  str(board == select_board_solution('e1')))


if __name__ == '__main__':
    tests()