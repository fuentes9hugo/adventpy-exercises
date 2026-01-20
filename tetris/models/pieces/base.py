from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color: str):
        self.shape: list[list[str]] = self._get_shape()
        self.color: tuple[str, str] = color


    def __repr__(self):
        return f"{self.__class__.__name__}(form={self.shape!r}, color={self.color!r})"
    

    def __str__(self):
        return "\n".join([self.color[0] + "".join(row) + self.color[1] for row in self.shape])


    def __eq__(self, other: "Piece"):
        if not isinstance(other, Piece):
            return NotImplemented
        
        return self.shape == other.shape

    @abstractmethod
    def _get_shape(self):
        pass


    def rotate_form(self, side: str):
        new_form = []

        for rows in zip(*self.shape):
            new_row = [char for char in rows]
            new_form.append(new_row if side == "left" else new_row[::-1])

        self.shape = new_form