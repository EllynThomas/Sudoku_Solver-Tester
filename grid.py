from enum import Enum

class SG_Type(Enum):
    ROW = 1
    COLUMN = 2
    SQUARE = 3      

class Sub_Grid:
    # A Row, Column, or Square
    # Saves the type of subgrid and the number of the subgrid

    def __init__(self, sub_grid_type, coord, grid):
        self.sub_grid_type = sub_grid_type

        if sub_grid_type == SG_Type.ROW:
            self.sub_grid_number = coord[0]
        elif sub_grid_type == SG_Type.COLUMN:
            self.sub_grid_number = coord[1]
        elif sub_grid_type == SG_Type.SQUARE:
            self.sub_grid_number = 3 * (coord[0] // 3) + coord[1] // 3

        self.sub_grid = None

        self.update(grid)
        self.covered = []

    def __call__(self): 
        return self.sub_grid

    def update(self, grid):
        # Updates the subgrid to the current state of the grid


        if self.sub_grid_type == SG_Type.ROW:
            self.sub_grid = grid[self.sub_grid_number]
        elif self.sub_grid_type == SG_Type.COLUMN:
            self.sub_grid = [grid[i][self.sub_grid_number] for i in range(9)]
        elif self.sub_grid_type == SG_Type.SQUARE:
            self.sub_grid = [grid[(self.sub_grid_number // 3) * 3 + i][(self.sub_grid_number % 3) * 3 + j] for i in range(3) for j in range(3)]

    def __call__(self):
        return self.sub_grid
    
    def cover(self, coord):
        # Covers the cell at the coordinate
        self.covered.append((coord, self.sub_grid[coord[0]][coord[1]]))
        self.sub_grid[coord[0]][coord[1]] = 'C'

    def uncover(self):
        # Uncovers the last cell covered
        # returns False if no cells are covered

        if len(self.covered) == 0:
            return False
        
        coord, number = self.covered.pop()
        self.sub_grid[coord[0]][coord[1]] = number
        return True

    def candidates(self):
        # returns a list of all the numbers that are not 
        # filled in the set
        if not self.sub_grid:
            raise ValueError("Subgrid not updated")
        return [i for i in range(1, 10) if i not in self.sub_grid]
    
    def coord(self, index):
        # returns the coordinates of the cell at the index
        if self.sub_grid_type == SG_Type.ROW:
            return self.sub_grid_number, index
        elif self.sub_grid_type == SG_Type.COLUMN:
            return index, self.sub_grid_number
        elif self.sub_grid_type == SG_Type.SQUARE:
            return 3 * (self.sub_grid_number // 3) + index // 3, 3 * (self.sub_grid_number % 3) + index % 3
    
    def coord_list(self):
        # returns a list of all coordinates in the subgrid
        return [self.coord(i) for i in range(9)]

    def index(self, coord):
        # returns the index of the cell at the coordinate
        if self.sub_grid_type == SG_Type.ROW:
            if coord[0] != self.sub_grid_number:
                raise ValueError("Coordinate not in row")    
            return coord[1]
        
        elif self.sub_grid_type == SG_Type.COLUMN:
            if coord[1] != self.sub_grid_number:
                raise ValueError("Coordinate not in column")
            return coord[0]
        
        elif self.sub_grid_type == SG_Type.SQUARE:
            if 3 * (coord[0] // 3) + coord[1] // 3 != self.sub_grid_number:
                raise ValueError("Coordinate not in square")
            return 3 * (coord[0] % 3) + coord[1] % 3
        

class Grid:
    # Grid of the pencil markings of a sudoku puzzle

    def __init__(self, grid):
        self.grid = grid
        
        self.pencil_grid = [[[] for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.pencil_grid[i][j] = 'F'
                else:
                    self.pencil_grid[i][j] = [k for k in range(1, 10)]

    def __call__(self):
        return self.grid

    def print_grid(self):
        # Prints the grid
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

    def square_number(coord):
        # Returns the square number of the cell at coord
        return 3 * (coord[0] // 3) + coord[1] // 3
    
    def square_index(coord):
        # Returns the index of the cell in the square
        return 3 * (coord[0] % 3) + coord[1] % 3
    
    def square_coord(sqr_num, index):
        # Returns the coordinate of the cell in the square
        return 3 * (sqr_num // 3) + index // 3, 3 * (sqr_num % 3) + index % 3
    
    def update_cell(self, coord, number):
        # Updates the grid with the number at the coordinate

        if self.grid[coord[0]][coord[1]] != 0:
            raise ValueError("Cell already filled")
        
        self.grid[coord[0]][coord[1]] = number
        self.pencil_fill(coord)



    def empty_cells(self):
        # Returns a list of all the empty cells
        return [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]
    
    def incomplete_cells(self, sub_grid):
        # Returns a list of indexes of incomplete cells in a subgrid
        return [i for i in range(9) if sub_grid[i] == 0]
    
    def incomplete_sets(self):
        # Returns list of incomplete sets
        # returns a rows, columns, squares with its index

        rows = [Sub_Grid(SG_Type.ROW, (i, 0)) for i in range(9)]
        rows= [r for r in rows if 0 in r()]

        cols = [Sub_Grid(SG_Type.COLUMN, (0, i)) for i in range(9)]
        cols = [c for c in cols if 0 in c()]

        sqrs = [Sub_Grid(SG_Type.SQUARE, (i // 3, i % 3)) for i in range(9)]
        sqrs = [s for s in sqrs if 0 in s()]

        return rows, cols, sqrs



    

    ### PENCIL FUNCTIONS ###

    def pencil_remove(self, coord, number):
        # Removes number from pencil marks
        if number in self.grid[coord[0]][coord[1]]:
            self.grid[coord[0]][coord[1]].remove(number)
            

    def pencil_cell(self, coord):
        # Returns the pencil marks of the cell
        self.pencil_prune(coord)
        return self.pencil_grid[coord[0]][coord[1]]
    
    def pencil_sub_grid(self, sub_grid):
        # Returns a set of all pencil marks of the subgrid
        coords = sub_grid.coord_list()
        pencils = set()
        for coord in coords:
            if self.pencil_cell(coord) != 'F':
                pencils.update(self.Pencil.cell(coord))
        return pencils

    
    def pencil_fill(self, coord):
        # Fills in the pencil mark cell
        self.grid[coord[0]][coord[1]] = 'F'
    
    def pencil_prune(self, coord):
        # Removes pencil marks if the number is already in any
        # of the subgrids of the cell
        row = Sub_Grid(SG_Type.ROW, coord, self.grid)
        col = Sub_Grid(SG_Type.COLUMN, coord, self.grid)
        sqr = Sub_Grid(SG_Type.SQUARE, coord, self.grid)

        candidates = set(row.candidates() + col.candidates() + sqr.candidates())
        self.pencil_grid[coord[0]][coord[1]] = [i for i in self.pencil_grid[coord[0]][coord[1]] if i in candidates]
    
    def pencil_remove_subgrids(self, coord, number):
        # Removes pencil marks of all pencil marks in the subgrids
        # of the cell

        for i in range(9):
            if number in self.pencil_grid[coord[0]][i]:
                self.pencil_grid[coord[0]][i].remove(number)

            if number in self.pencil_grid[i][coord[1]]:
                self.pencil_grid[i][coord[1]].remove(number)

            if number in self.pencil_grid[3 * (coord[0] // 3) + i // 3][3 * (coord[1] // 3) + i % 3]:
                self.pencil_grid[3 * (coord[0] // 3) + i // 3][3 * (coord[1] // 3) + i % 3].remove(number)






