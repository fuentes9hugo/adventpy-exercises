from .pieces import Piece, O, I, T, S, Z, L, J

from random import choice


class Board:
    ROWS: int = 20
    COLS: int = 10

    def __init__(self):
        self._grid: list[list[str]] = self._make_grid()
        self._current_piece: Piece = None


    def __repr__(self):
        return f"{self.__class__.__name__}(grid={self._grid!r}, current_piece={self._current_piece!r})"


    @property
    def grid(self):
        return self._grid
    

    @property
    def current_piece(self):
        return self._current_piece


    @current_piece.setter
    def current_piece(self, piece: Piece):
        if isinstance(piece, Piece): self._current_piece = piece


    def _make_grid(self):
        return [["##" if j == 0 or j == self.COLS + 1 else "  " for j in range(self.COLS + 2)]
                if i != self.ROWS else ["##"] * (self.COLS + 2) for i in range(self.ROWS + 1)]
    

    def insert_piece(self):
        piece_len = len(self._current_piece.shape)
        y = self.COLS // 2 - piece_len // 2 + (1 if piece_len % 2 == 0 else 0)

        for i, row in enumerate(self._current_piece.shape):
            for j, char in enumerate(row, start=y):
                if char == "[]":
                    self._grid[i][j] = char