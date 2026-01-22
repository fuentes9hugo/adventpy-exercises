from .pieces import Piece, O, I, T, S, Z, L, J

from random import choice
from collections import deque


class Board:
    ROWS: int = 20
    COLS: int = 10

    def __init__(self):
        self._grid: deque[list[str]] = self._make_grid()
        self._current_piece: Piece = None


    def __repr__(self):
        return f"{self.__class__.__name__}(grid={self._grid!r}, current_piece={self._current_piece!r})"


    @property
    def grid(self):
        return self._grid


    @property
    def current_piece(self):
        return self._current_piece


    # --- NO ES NECESARIO, SIMPLEMENTE LO TENGO COMO ANOTACIÓN ---
    # Los getters y setters, si no ofrecen ninguna funcionalidad, por ejemplo: el setter no valida nada porque tienes todos los datos controlados, etc.
    # y el getter solo devuelve el valor del atributo siendo este privado
    # Es mejor ahorrárselos
    @current_piece.setter
    def current_piece(self, piece: Piece):
        if isinstance(piece, Piece): self._current_piece = piece


    # Empty grid generation
    def _make_grid(self):
        return deque([["##" if j == 0 or j == self.COLS + 1 else "  " for j in range(self.COLS + 2)]
                if i != self.ROWS else ["##"] * (self.COLS + 2) for i in range(self.ROWS + 1)])


    # 1. Choose a piece type randomly
    # 2. Calculate the insertion column based on the piece's length
    # 3. Set the piece's grid position for future tracking
    def insert_piece(self):
        self._current_piece = choice(Piece.__subclasses__())()

        piece_len = len(self._current_piece.shape)
        y = (self.COLS + 2) // 2 - piece_len // 2 - (0 if piece_len % 2 == 0 else 1)

        self._current_piece.grid_position = [0, y]

        for i, row in enumerate(self._current_piece.shape):
            for j, char in enumerate(row, start=y):
                if "[]" in char:
                    self._grid[i][j] = char