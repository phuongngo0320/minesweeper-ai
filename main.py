from libs.gameplay import random_play
from src.board import Board
from src.minesweeper import Minesweeper

board = Board(5, 7)
game = Minesweeper(board)
game.play(random_play, verbose=True)