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

    
    def __str__(self):
        return "\n".join(["".join(row) for row in self._grid])


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

        if not self._can_move(0, y): return False

        self._current_piece.grid_position = [0, y]

        return True

    
    def _can_move(self, pos_y: int, pos_x):
        if any("[]" in self._grid[i][j] or self._grid[i][j] == "##"
               for i, row in enumerate(self._current_piece.shape, start=pos_y)
               for j, char in enumerate(row, start=pos_x)
               if "[]" in char):
            return False
        
        return True


    def move_piece_down(self):
        x, y = self._current_piece.grid_position
        x += 1

        if self._can_move(x, y):
            self._current_piece.grid_position = (x, y)
            return True

        return False
    

    def move_piece_horizontally(self, side: str):
        x, y = self._current_piece.grid_position

        if side == "d": # right
            y += 1
            if self._can_move(x, y): self._current_piece.grid_position = [x, y]
        
        elif side == "a": # left
            y -= 1
            if self._can_move(x, y): self._current_piece.grid_position = [x, y]

    
    def rotate_current_piece(self, side: str):
        self.current_piece.rotate(side)
        # TODO: check if the piece is able to rotate


    def draw(self):
        grid_to_draw = [row[:] for row in self._grid] # DEEP COPY -> if you do self._grid.copy() it just copies the main list but none of the lists inside
        x, y = self._current_piece.grid_position

        for i, row in enumerate(self._current_piece.shape, start=x):
            for j, char in enumerate(row, start=y):
                if "[]" in char: grid_to_draw[i][j] = char

        return "\n".join(["".join(row) for row in grid_to_draw])
    

    # TODO: comment the new code