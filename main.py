from src.board import Board
from src.minesweeper import Minesweeper
from src.strategy import random_play

board = Board(5, 7)
print(board.check_input())
# game = Minesweeper(board)
# game.play(random_play, verbose=True)