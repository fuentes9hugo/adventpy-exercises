from .base import Piece


class Square(Piece):
    def __init__(self):
        super().__init__(color=("\033[33m", "\033[0m")) # Yellow

    
    def _get_shape(self):
        return [
            ["[]", "[]"],
            ["[]", "[]"]
        ]