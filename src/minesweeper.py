from typing import Callable
from src.board import Board
from src.move import Move

class Minesweeper:
    
    def __init__(self, initial: Board) -> None:
        self.width = initial.width
        self.height = initial.height
        self.initial = initial
        
        self.positions = {
            (x, y)
            for x in range(initial.width)
            for y in range(initial.height)
        }
        
    def actions(self, state: Board):
        covered =  list(self.positions - set(state.uncovered.keys()))
        
        moves = []
        for pos in covered:
            moves.append(Move(pos, flag=True))
            moves.append(Move(pos, flag=False))
        
        return moves
    
    def result(self, state: Board, move: Move):
        
        result = None
        if move.flag:
            result = state.flag(*move.pos)
        else:
            result = state.uncover(*move.pos)
        
        return result
    
    def is_terminal(self, state: Board):
        
        return (
            state.game_over or 
            len(state.uncovered) == len(self.positions)
        )

    def play(self, strategy: Callable[['Minesweeper', Board], Move], verbose=False):
        
        state = self.initial
        while not self.is_terminal(state):
            move = strategy(self, state)
            state = self.result(state, move)
            if verbose:
                print(state)
        return state
        
        
        
        