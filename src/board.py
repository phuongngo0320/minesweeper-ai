from copy import deepcopy
import random
from src.cell import Cell

class Board:
    
    def __init__(self, height, width) -> None:
        self.width = width
        self.height = height
        self.map = [[
                Cell(0)
                for j in range(width)
            ]
            for i in range(height)
        ]
        
        self.uncovered = dict()
        self.game_over = False
        i = 0
        while i < int((width*height)/5) :
            row_pos = random.randint(0,height-1)
            col_pos = random.randint(0,width-1)
            if self.at(row_pos,col_pos).mine == True: continue
            else:
                self.add_mine(row_pos,col_pos)
                i+=1

        
    def out_of_range(self, row, col):
        if 0 <= col < self.width and 0 <= row < self.height:
            return False
        return True
        
    def at(self, row, col) -> Cell:
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
    
    def add_mine(self,x,y):
        self.map[x][y].mine = True
        for dx, dy in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
            if self.out_of_range(x+dx,y+dy):
                continue
            else:
                self.at(x+dx,y+dy).number += 1   
    
    def dump(self) -> str:
        def row_str(row):
            return ' '.join(
                self.at(row, col).dump()
                for col in range(self.width)
            )
        return '\n'.join(
            map(row_str, range(self.height))
        ) + '\n'
    
    def __repr__(self) -> str:
        def row_str(row):
            return ' '.join(
                str(self.at(row, col))
                for col in range(self.width)
            )
        return '\n'.join(
            map(row_str, range(self.height))
        ) + '\n'
    
 

