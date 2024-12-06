from abc import ABC

class HouseRule(ABC):
    """This is an abstract class for sudoku rules that apply to a House. 
    A house is a row, column or square in a sudoku puzzle"""
        
    def evaluate(self, house):
        """Evaluates the rule. Returns the number and index if the rule applies, else returns None, None"""
        pass

    def __str__(self):
        """Returns the name of the rule"""
        pass
    

class CellRule(ABC):
    """This is an abstract class for sudoku rules that apply to a single cell. """
        
    def evaluate(self, coord, grid):
        """Evaluates the rule to a cell. Returns the number if the rule applies, else returns None"""
        pass

    def __str__(self):
        """Returns the name of the rule"""
        pass
    


class PencilHouseRule(ABC):
    """This is an abstract class for pencil marking rules that apply to a house. """
        
    def evaluate(self, house):
        """Evaluates the rule. Returns the list of possible numbers that can go in a cell"""
        pass

    def __str__(self):
        """Returns the name of the rule"""
        pass

class PencilCellRule(ABC):
    """This is an abstract class for pencil marking rules that apply to a single cell. """
        
    def evaluate(self, coord, grid):
        """Evaluates the rule to a cell. Returns the list of possible numbers that can go in a cell"""
        pass

    def __str__(self):
        """Returns the name of the rule"""
        pass