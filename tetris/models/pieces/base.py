from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color: tuple[str, str]) -> None:
        self._color: tuple[str, str] = color
        self.shape: list[list[str]] = self._get_shape()
        self.grid_position: list[int] = []


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(shape={self.shape!r}, color={self._color!r})"


    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.shape])


    def __eq__(self, other: "Piece") -> bool:
        if not isinstance(other, Piece):
            return NotImplemented
        
        return self.shape == other.shape and self._color == other._color


    @property
    def color(self) -> tuple[str, str]:
        return self._color
    

    # Gets the piece's shape uncolorized
    @abstractmethod
    def _raw_shape(self) -> list[list[str]]:
        pass

    
    # Colorize the piece's shape
    def _get_shape(self) -> list[list[str]]:
        shape = self._raw_shape()

        for i, row in enumerate(shape):
            if "[]" in row:
                for j, char in enumerate(row):
                    if char == "[]":
                        shape[i][j] = self._color[0] + "[]" + self._color[1]

        return shape


    # Rotate the piece in 2 different ways: right and left
    def rotate(self, side: str) -> None:
        new_form = []

        if side == "right": # right
            for rows in zip(*self.shape):
                new_row = [char for char in rows[::-1]]
                new_form.append(new_row)

        elif side =="left": # left
            for rows in zip(*[row[::-1] for row in self.shape]):
                new_row = [char for char in rows]
                new_form.append(new_row)

        self.shape = new_form if new_form else self.shape