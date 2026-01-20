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


    def rotate(self, side: str):
        new_form = []
        
        if side == "right":
            for rows in zip(*self.shape):
                new_row = [char for char in rows[::-1]]
                new_form.append(new_row)

        elif side =="left":
            for rows in zip(*[row[::-1] for row in self.shape]):
                new_row = [char for char in rows]
                new_form.append(new_row)

        self.shape = new_form if new_form else self.shape