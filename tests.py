from solve import *

# Sudoku boards for testing

def select_board(board):
    """
    Selects a board from the list of sample boards
    """

    # Very easy
    
    if board == 've1':
        # Only requires last free cell
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
        # Also requires Naked_Single
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
        # Also requires Hidden Single, + more to add
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


def select_board_steps(board):
    """
    Selects the number of steps to solve a board
    """
    if board == 've1':
        return 10
    elif board == 'e1':
        return 45
    elif board == 'h1':
        return 60
    else:
        return None
    

def hard_1():
    """
    Hard 1
    """
    board = Board(select_board('e1'))
    solution = select_board_solution('e1')
    steps = select_board_steps('e1')
    board.print_board()

    for i in range(steps):
        print('Step', i+1)
        if not solve_step(board):
            print('No more steps')
            break
        print(' ')


    board.print_board()
    print('Matches solution? ' +  str(str(board) == str(solution)))


def tests():
    """
    Runs tests for the solve_step function
    """
    hard_1()


if __name__ == '__main__':
    tests()