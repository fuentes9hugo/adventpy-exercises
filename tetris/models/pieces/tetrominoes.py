from .base import Piece


class O(Piece):
    def __init__(self):
        super().__init__(color=("\033[33m", "\033[0m")) # Yellow

    
    def _get_shape(self):
        return [
            ["[]", "[]"],
            ["[]", "[]"]
        ]


class I(Piece):
    def __init__(self):
        super().__init__(color=("\033[36m", "\033[0m")) # Cyan

    
    def _get_shape(self):
        return [
            ["[]", "[]", "[]", "[]"]
        ]
    

class T(Piece):
    def __init__(self):
        super().__init__(color=("\033[35m", "\033[0m")) # Purple

    
    def _get_shape(self):
        return [
            ["  ", "[]", "  "],
            ["[]", "[]", "[]"]
        ]


class S(Piece):
    def __init__(self):
        super().__init__(color=("\033[31m", "\033[0m")) # Red

    
    def _get_shape(self):
        return [
            ["  ", "[]", "[]"],
            ["[]", "[]", "  "]
        ]
    

class Z(Piece):
    def __init__(self):
        super().__init__(color=("\033[32m", "\033[0m")) # Green

    
    def _get_shape(self):
        return [
            ["[]", "[]", "  "],
            ["  ", "[]", "[]"]
        ]
    

class L(Piece):
    def __init__(self):
        super().__init__(color=("\033[38;5;208m", "\033[0m")) # Orange

    
    def _get_shape(self):
        return [
            ["  ", "  ", "[]"],
            ["[]", "[]", "[]"]
        ]
    

class J(Piece):
    def __init__(self):
        super().__init__(color=("\033[38;5;205m", "\033[0m")) # Pink

    
    def _get_shape(self):
        return [
            ["[]", "  ", "  "],
            ["[]", "[]", "[]"]
        ]