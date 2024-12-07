
class Board:
    """ Repersents a sudoku board. 
    Includes both the grid and the pencil marks grid.
    Pencil mark grid starts with all possible candidates - so the solver
    only needs to remove (never add) candidates as it goes along."""

    def __init__(self, grid):
        self.grid = grid
        self.pencil_grid = [[set() for i in range(9)] for j in range(9)]

        # Remove pencil marks from filled cells
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.pencil_grid[i][j] = set('F') # Filled
                else:
                    self.pencil_grid[i][j] = set(range(1, 10))

    def __str__(self):
        return str(self.grid)

    def print_board(self):
        print(''.join(['-' for i in range(25)]))
        for i in range(9):
            print('|', end = '')
            for j in range(9):
                print(f' {self.grid[i][j]}', end = '')
                if j % 3 == 2:
                    print(' |', end = '')
            print()
            if i % 3 == 2:
                print(''.join(['-' for i in range(25)]))
        
        print()


    def row(self, row_num):
        # Returns a row of the board
        return self.grid[row_num]
    
    def col(self, col_num):
        # Returns a column of the board
        return [self.grid[i][col_num] for i in range(9)]
    
    def sqr(self, sqr_num):
        # Returns a square of the board
        return [self.grid[(sqr_num // 3) * 3 + i][(sqr_num % 3) * 3 + j] for i in range(3) for j in range(3)]
    
    def sqr_number(self, coord):
        # Returns the square number for a given coordinate
        return 3 * (coord[0] // 3) + coord[1] // 3
    
    def sqr_coord(self, sqr_number, index):
        # Converts a square number and index to a coordinate
        return 3 * (sqr_number // 3) + index // 3, 3 * (sqr_number % 3) + index % 3
    
    def sqr_index(self, coord):
        # Returns the index of a cell in a square
        return 3 * (coord[0] % 3) + coord[1] % 3
    
    def houses(self, coord):
        # Returns the row, column, and square for a given coordinate
        return self.row(coord[0]), self.col(coord[1]), self.sqr(self.sqr_number(coord))


    
    def place_number(self, coord, number):
        # Places a number in a cell on the board
        if self.grid[coord[0]][coord[1]] != 0:
            print(f"Cell ({coord[0]}, {coord[1]}) already filled")
        
        self.grid[coord[0]][coord[1]] = number
        self.pencil_grid[coord[0]][coord[1]] = 'F'
    
    def empty_cells(self):
        # Returns a list of coordinates of all empty cells
        return [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]
    
    
    def incomplete_houses(self):
        # Returns lists of rows, columns, squares with the indexes
        # of the incomplete houses

        rows = [(self.row(i), i) for i in range(9)]
        rows = [r for r in rows if 0 in r[0]]

        cols = [(self.col(i), i) for i in range(9)]
        cols = [c for c in cols if 0 in c[0]]

        sqrs = [(self.sqr(i), i) for i in range(9)]
        sqrs = [s for s in sqrs if 0 in s[0]]

        return rows, cols, sqrs


    
    def remove_pencil(self, coord, number):
        # Removes a pencil mark from a cell
        self.pencil_grid[coord[0]][coord[1]].discard(number)

    
    def prune_pencil(self, coord):
    # Removes all pencil marks for numbers that are already
    # in one of the cells houses
        eliminated = set(self.row(coord[0]) + self.col(coord[1]) \
                         + self.sqr(self.sqr_number(coord)))
        for number in eliminated:
            self.remove_pencil(coord, number)

    def pencil_cell(self, coord):
        # Returns the pencil marks for a cell
        self.prune_pencil(coord) # Always prune before returning
        return self.pencil_grid[coord[0]][coord[1]]
    




    