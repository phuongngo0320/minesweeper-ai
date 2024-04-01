from copy import deepcopy
import random
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
        
        for i in range(0,int(width*height/5)):
            x_pos = random.randint(0,width-1)
            y_pos = random.randint(0,height-1)
            if self.at(x_pos,y_pos).mine == True: continue
            else:
                self.add_mine(x_pos,y_pos)
                i+=1

    def out_of_range(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return False
        return True
        
    def at(self, x, y) -> Cell:
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
    
    def add_mine(self,x,y):
        self.at(x,y).mine = True
        for dx, dy in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
            if self.out_of_range(x+dx,y+dy):
                continue
            else:
                self.at(x+dx,y+dy).number += 1

