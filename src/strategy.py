import random
from src.board import Board
from src.minesweeper import Minesweeper

def random_play(game: Minesweeper, state: Board):
    return random.choice(list(game.actions(state)))

# TODO: blind search

# TODO: heuristic search