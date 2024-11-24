# Contains all techniques to fill a cell in a sudoku puzzle
from checks import *
from abstractclasses import *
from grid import *



### Sub Grid Techniques ###

class lfc_rule(SetRule):
    # Last Free Cell Rule
    # Only one cell in a set left to fill
    # Updates a cell if applicable and returns number, coord if true, else returns None, None
    def evaluate(self, sub_grid, grid):
        candidates = sub_grid.candidates()

        if len(candidates) == 1:
            coord = sub_grid.coord(sub_grid.incomplete_cells()[0])
            grid.update_cell(coord, candidates[0])
            return candidates[0], coord
        return None, None
    
    def __str__(self):
        return "Last Free Cell Rule"



### Cell Techniques ###

class ns_rule(CellRule):
    # Naked Single Rule
    # Only one number can go in a cell
    # Updates a cell if applicable and returns number, coord if true, else returns None, None
    def evaluate(self, coord, grid):
        candidates = grid.pencil_cell(coord)
        if len(candidates) == 1:
            grid.update_cell(coord, candidates[0])
            return candidates[0], coord
        return None, None
    
    def __str__(self):
        return "Naked Single Rule"
    
    


class uc_rule(CellRule):
    # Unique Candidate Rule
    # Only one cell in a row, column or square can contain a number
    # Updates a cell if applicable and returns number, coord if true, else returns None, None
    def evaluate(self, coord, grid, pencil_grid):
        pencil = pencil_grid.cell(coord)
        
        row_sg_pencil = self.cover_and_check(coord, grid, SG_Type.ROW)
        
        col_sg_pencil = self.cover_and_check(coord, grid, SG_Type.COLUMN)
        
        sqr_sg_pencil = self.cover_and_check(coord, grid, SG_Type.SQUARE)

        for candidate in pencil:
            if candidate not in row_sg_pencil or candidate not in col_sg_pencil or candidate not in sqr_sg_pencil:
                Grid.update_cell(coord, candidate)
                return candidate, coord
        
        return None, None
    
    def __str__(self):
        return "Unique Candidate Rule"
    
    def cover_and_check(self, coord, grid, sg_type):
        # covers the cell in at the coord and returns the set of candidates
        sub_grid = Sub_Grid(sg_type, coord)

        sub_grid.cover(coord)
        return grid.pencil_sub_grid(sub_grid)



### Pencil Marking Techniques ###








