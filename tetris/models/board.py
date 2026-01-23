from .pieces import Piece, O, I, T, S, Z, L, J

from random import choice
from collections import deque
from copy import deepcopy


class Board:
    ROWS: int = 20
    COLS: int = 10

    def __init__(self) -> None:
        self._grid: deque[list[str]] = self._make_grid()
        self._current_piece: Piece = None


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(grid={self._grid!r}, current_piece={self._current_piece!r})"


    # Draw the board's grid without the current piece, just with the pieces played before (for debugging)
    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._grid])


    @property
    def grid(self) -> deque[list[str]]:
        return self._grid


    @property
    def current_piece(self) -> Piece:
        return self._current_piece


    # --- NO ES NECESARIO, SIMPLEMENTE LO TENGO COMO ANOTACIÓN ---
    # Los getters y setters, si no ofrecen ninguna funcionalidad, por ejemplo: el setter no valida nada porque tienes todos los datos controlados, etc.
    # y el getter solo devuelve el valor del atributo siendo este privado
    # Es mejor ahorrárselos
    @current_piece.setter
    def current_piece(self, piece: Piece) -> None:
        if isinstance(piece, Piece): self._current_piece = piece


    # Empty grid generation
    def _make_grid(self) -> deque[list[str]]:
        return deque([["##"] + ["  " for _ in range(self.COLS)] + ["##"] if i < self.ROWS else ["##"] * (self.COLS + 2) for i in range(self.ROWS + 1)])


    # 1. Choose a piece type randomly
    # 2. Calculate the insertion column based on the piece's length
    # 3. Set the piece's grid position for future tracking
    def insert_piece(self) -> bool:
        self._current_piece = choice(Piece.__subclasses__())()

        piece_len = len(self._current_piece.shape)
        x = (self.COLS + 2) // 2 - piece_len // 2 - (0 if piece_len % 2 == 0 else 1)

        if not self._can_move(0, x): return False

        self._current_piece.grid_position = [0, x]

        return True

    
    # Check if the current piece is allowed to rotate or to move
    def _can_move(self, pos_y: int, pos_x, piece:Piece=None) -> bool:
        if not piece: piece = self._current_piece

        if any("[]" in self._grid[i][j] or self._grid[i][j] == "##"
               for i, row in enumerate(piece.shape, start=pos_y)
               for j, char in enumerate(row, start=pos_x)
               if "[]" in char):
            return False
        
        return True


    # Move the current piece one row down
    def move_piece_down(self) -> bool:
        y, x = self._current_piece.grid_position
        y += 1

        if self._can_move(y, x):
            self._current_piece.grid_position = (y, x)
            return True

        return False
    

    # Move the current piece one column to the right or to the left, depending on the user's choice
    def move_piece_horizontally(self, side: str) -> None:
        y, x = self._current_piece.grid_position

        if side == "d": # right
            x += 1
            if self._can_move(y, x): self._current_piece.grid_position = [y, x]
        
        elif side == "a": # left
            x -= 1
            if self._can_move(y, x): self._current_piece.grid_position = [y, x]

    
    # Rotate the piece is allowed to rotate
    # If it is not allowed, check if moving the piece horizontally allows it to rotate
    def rotate_current_piece(self, side: str) -> None:
        aux_piece = deepcopy(self._current_piece)
        aux_piece.rotate(side)
        y, x = aux_piece.grid_position
        
        if self._can_move(y, x, piece=aux_piece):
            self._current_piece.rotate(side)
        
        elif self._can_move(y, x + 1, piece=aux_piece):
            self._current_piece.grid_position = [y, x + 1]
            self._current_piece.rotate(side)

        elif self._can_move(y, x - 1, piece=aux_piece):
            self._current_piece.grid_position = [y, x - 1]
            self._current_piece.rotate(side)


    # Draw the board's grid with the current piece and the pieces played before
    def draw(self) -> str:
        grid_to_draw = [row[:] for row in self._grid] # DEEP COPY -> if you do self._grid.copy() it just copies the main list but none of the lists inside
        y, x = self._current_piece.grid_position

        for i, row in enumerate(self._current_piece.shape, start=y):
            for j, char in enumerate(row, start=x):
                if "[]" in char: grid_to_draw[i][j] = char

        return "\n".join(["".join(row) for row in grid_to_draw])
    

    # Check if the piece is toching a bottom limit ('##' or any '[]')
    # TODO: check if this funcition works correctly
    def check_bottom_limit(self) -> bool:
        y, x, piece_bottom = next((self._current_piece.grid_position[0] + len(self._current_piece) - i, self._current_piece.grid_position[1], [row])
                             for i, row in enumerate(reversed(self._current_piece)) if "[]" in row)
        
        return not self._can_move(y, x, piece_bottom)