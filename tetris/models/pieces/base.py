from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color: str):
        self.form: list[list[str]] = self._get_form()
        self.color: str = color


    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color!r}, form={self.form!r})"
    

    def __str__(self):
        return "\n".join(["".join(row) for row in self.form])


    def __eq__(self, other: "Piece"):
        if not isinstance(other, Piece):
            return NotImplemented
        
        return self.form == other.form

    @abstractmethod
    def _get_form(self):
        pass


    def rotate_form(self, side: str):
        new_form = []

        for rows in zip(*self.form):
            new_row = [char for char in rows]
            new_form.append(new_row if side == "left" else new_row[::-1])

        self.form = new_form