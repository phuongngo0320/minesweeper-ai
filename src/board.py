from copy import deepcopy
from src.cell import Cell

class Board:
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.map = [
            [Cell()] * width
            for i in height
        ]
        
        self.uncovered = dict()
        self.game_over = False
        
    def out_of_range(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return False
        return True
        
    def at(self, x, y):
        if self.out_of_range(x, y):
            raise Exception("Board: out of range")
        return self.map[x][y]
    
    def uncover(self, x, y):
        board = deepcopy(self)
    
        if board.out_of_range(x, y):
            raise Exception("Board: out of range")
        
        if board.at(x, y).flag:
            raise Exception("Uncovering a flagged cell")
        
        if not board.at(x, y).covered:
            raise Exception("Uncovering an uncovered cell")
        
        board.map[x][y].covered = False
        
        if board.at(x, y).mine:
            board.game_over = True
        else:
            board.uncovered[(x, y)] = self.map[x][y]
            
        return board
    
    def flag(self, x, y):
        board = deepcopy(self)
        
        if board.out_of_range(x, y):
            raise Exception("Board: out of range")
        
        if board.at(x, y).flag:
            raise Exception("Flagging a flagged cell")
        
        board.map[x][y].flag = True    
        
        return board
    
    def __repr__(self) -> str:
        def row(y):
            return ' '.join(
                self.at(x, y) 
                for x in range(self.width)
            )
        return '\n'.join(
            map(row, range(self.height))
        ) + '\n'
    