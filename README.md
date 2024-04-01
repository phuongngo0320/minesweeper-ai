# minesweeper-ai
A simple bot that can solve Minesweeper puzzles (faster)

## Usage

```py
# main.py
from src.board import Board
from src.minesweeper import Minesweeper
import src.strategy as strat

board = Board(9, 9)
game = Minesweeper(board)
game.play(strat.random_play, verbose=True)
```
