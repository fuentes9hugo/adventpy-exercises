from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self):
        self.form: list[list[str]] = self._get_form()


    def __repr__(self):
        return f"{self.__class__.__name__}(form='{self.form!r}')"
    

    def __str__(self):
        return "\n".join(["".join(row) for row in self.piece])


    def __eq__(self, value):
        if not isinstance(value, Piece):
            return NotImplemented
        
        return self.form == value.form

    @abstractmethod
    def _get_form(self):
        pass


    def _rotate_form(self, side):
        new_form = []

        for rows in zip(*self.form):
            new_row = [char for char in rows]
            new_form.append(new_row if side == "left" else reversed(new_row))

        self.form = new_form