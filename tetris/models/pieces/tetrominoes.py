from .base import Piece


class O(Piece):
    def __init__(self) -> None:
        color = ("\033[33m", "\033[0m") # Yellow
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["[]", "[]"],
            ["[]", "[]"]
        ]


    # Rewrite this function for this piece because it doesn't change anything
    # The shape is the same rotateed or not
    def rotate(self, side: str) -> None:
        pass


class I(Piece):
    def __init__(self) -> None:
        color = ("\033[36m", "\033[0m") # Cyan
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["  ", "  ", "  ", "  "],
            ["[]", "[]", "[]", "[]"],
            ["  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  "]
        ]


class T(Piece):
    def __init__(self) -> None:
        color = ("\033[35m", "\033[0m") # Purple
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["  ", "[]", "  "],
            ["[]", "[]", "[]"],
            ["  ", "  ", "  "]
        ]


class S(Piece):
    def __init__(self) -> None:
        color = ("\033[31m", "\033[0m") # Red
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["  ", "[]", "[]"],
            ["[]", "[]", "  "],
            ["  ", "  ", "  "]
        ]


class Z(Piece):
    def __init__(self) -> None:
        color = ("\033[32m", "\033[0m") # Green
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["[]", "[]", "  "],
            ["  ", "[]", "[]"],
            ["  ", "  ", "  "]
        ]


class L(Piece):
    def __init__(self) -> None:
        color = ("\033[38;5;208m", "\033[0m") # Orange
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["  ", "  ", "[]"],
            ["[]", "[]", "[]"],
            ["  ", "  ", "  "]
        ]


class J(Piece):
    def __init__(self) -> None:
        color = ("\033[38;5;205m", "\033[0m") # Pink
        super().__init__(color)


    def _raw_shape(self) -> list[list[str]]:
        return [
            ["[]", "  ", "  "],
            ["[]", "[]", "[]"],
            ["  ", "  ", "  "]
        ]