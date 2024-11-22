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




def solve_step(board):
    """
    Solves a single step of a sudoku board.
    Prints what technique was used to solve the step
    The coordinates of the cell that was solved
    And returns the new board
    """

    # Check if the board is solved
    if check_fully_filled(board):
        print("Board is already solved")
        return board

    # Check for sole candidate
    board, solved = sole_candidate(board)
    if solved:
        print("Sole candidate")
        print(f"Solved cell: {solved}")
        return board

    # Check for last free cell
    board, solved = last_free_cell(board)
    if solved:
        print("Last free cell")
        print(f"Solved cell: {solved}")
        return board

    # If no technique was used, return the board
    print("No technique used")
    return board






# Sudoku boards

def select_board(board):
    """
    Selects a board from the list of sample boards
    """

    # Very easy
    # only uses last free cell
    if board == 've1':
        return     [[0, 3, 7, 1, 5, 2, 9, 4, 8],
                    [1, 2, 9, 8, 4, 7, 5, 3, 6],
                    [5, 0, 8, 6, 3, 9, 7, 2, 1],
                    [9, 7, 3, 2, 1, 5, 8, 6, 4],
                    [4, 1, 5, 7, 6, 0, 2, 9, 3],
                    [8, 6, 2, 4, 9, 3, 1, 5, 7],
                    [3, 9, 1, 5, 8, 6, 4, 7, 2],
                    [2, 5, 4, 3, 7, 1, 6, 8, 0],
                    [7, 8, 0, 9, 2, 4, 3, 1, 5]]
    

    # Easy
    # Uses last free cell and sole candidate
    elif board == 'e1':
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
    board = select_board('ve1')
    print_board(board)

    for i in range(5):
        board = solve_step(board)
    print_board(board)


if __name__ == '__main__':
    tests()