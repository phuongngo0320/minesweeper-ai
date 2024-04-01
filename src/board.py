from copy import deepcopy
from src.cell import Cell

class Board:
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.map = [
            [Cell(0)] * width
            for i in range(height)
        ]
        
        self.uncovered = dict()
        self.game_over = False
        
    def out_of_range(self, row, col):
        if 0 <= col < self.width and 0 <= row < self.height:
            return False
        return True
        
    def at(self, row, col):
        if self.out_of_range(row, col):
            raise Exception(f"Board {self.height}x{self.width} out of range: {row}, {col}")
        return self.map[row][col]
    
    def uncover(self, row, col):
        board = deepcopy(self)
    
        if board.out_of_range(row, col):
            raise Exception("Board: out of range")
        
        if board.at(row, col).flag:
            raise Exception("Uncovering a flagged cell")
        
        if not board.at(row, col).covered:
            raise Exception("Uncovering an uncovered cell")
        
        board.map[row][col].covered = False
        
        if board.at(row, col).mine:
            board.game_over = True
        else:
            board.uncovered[(row, col)] = self.map[row][col]
            
        return board
    
    def flag(self, row, col):
        board = deepcopy(self)
        
        if board.out_of_range(row, col):
            raise Exception("Board: out of range")
        
        if board.at(row, col).flag:
            raise Exception("Flagging a flagged cell")
        
        board.map[row][col].flag = True    
        
        return board
    
    def __repr__(self) -> str:
        def row_str(row):
            return ' '.join(
                str(self.at(row, col))
                for col in range(self.width)
            )
        return '\n'.join(
            map(row_str, range(self.height))
        ) + '\n'
    