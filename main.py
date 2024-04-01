from src.board import Board
from src.minesweeper import Minesweeper
from src.strategy import random_play

board = Board(9, 9)
game = Minesweeper(board)
game.play(random_play, verbose=True)