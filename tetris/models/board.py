from .pieces import Piece, O, I, T, S, Z, L, J

from random import choice


class Board:
    ROWS: int = 20
    COLS: int = 10

    def __init__(self):
        self._grid: list[list[str]]
        self._current_piece: Piece


    def __repr__(self):
        return f"{self.__class__.__name__}(grid={self._grid!r}, current_piece={self._current_piece!r})"


    @property
    def grid(self):
        return self.grid
    

    def _get_current_piece(self):
        self._current_piece = choice((Piece.__subclasses__()))