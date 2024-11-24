from checks import *
from rules import *
from grid import *


def do_rule(rule, grid):
    """
    Evaluates a rule to a grid
    Prints the rule, number, coord if applied
    Returns True if the rule was applied
    """
    if isinstance(rule, CellRule):
        empty_cells = grid.empty_cells()
        for cell in empty_cells:
            number = rule.evaluate(cell, grid)
            if number[0]:
                print(rule)
                print(f"{number} in : {cell}")
                return True
            
    elif isinstance(rule, SetRule):
        rows, cols, sqrs = grid.incomplete_sets()
        
        for row in rows:
            number, index = rule.evaluate(row, grid)
            if number[0]:
                print(rule)
                coord = (row[1], index)
                print(f"{number} in : {coord}")
                return True
        
        for col in cols:
            number, index = rule.evaluate(col, grid)
            if number[0]:
                print(rule)
                coord = (index, col[1])
                print(f"{number} in : {coord}")
                return True
        
        for sqr in sqrs:
            number, index = rule.evaluate(sqr, grid)
            if number:
                print(rule)
                coord = grid.square_coord(sqr[1], index)
                print(f"{number} in : {index}")
                return True
            
    else:
        return False


def solve_step(grid):
    """
    Solves a single step of a sudoku board.
    Returns the updated grid
    """
    # Check for naked single
    if do_rule(ns_rule(), grid):
        return grid
    
    # Check for unique candidate
    if do_rule(uc_rule(), grid):
        return grid
    
    # Check for last free cell
    if do_rule(lfc_rule(), grid):
        return grid


    # If no technique was used, return the board
    print("No technique used")
    return grid






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

    # easy 1
    board = Grid(select_board('e1'))
    board.print_grid()
    print(' ')


    for i in range(45):
        print('Step', i+1)
        board = solve_step(board)
        print(' ')

        # print_board(board)
        if check_valid_solution(board):
            print('Solved')
            break
    board.print_grid()
    print('Matches solution? ' +  str(board == select_board_solution('e1')))


if __name__ == '__main__':
    tests()