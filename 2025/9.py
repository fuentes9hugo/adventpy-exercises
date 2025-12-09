"""Los elfos han construido un reno 🦌 robot aspirador (@) para limpiar un poco el taller de cara a las navidades.

El reno se mueve sobre un tablero para recoger cosas del suelo (*) y debe evitar obstáculos (#).

Recibirás dos parámetros:

board: un string que representa el tablero.
moves: un string con los movimientos: 'L' (izquierda), 'R' (derecha), 'U' (arriba), 'D' (abajo).
Reglas del movimiento:

Si el reno se sale del tablero o choca contra un obstáculo (#) → devuelve 'crash'.
Si el reno recoge algo del suelo (*) durante los movimientos → devuelve 'success'.
Si el reno no recoge nada ni se estrella → devuelve 'fail'.
Importante: Ten en cuenta que en el board la primera y última línea están en blanco y deben descartarse."""


from typing import List, Literal


def moveReno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:
    board = board.strip().split("\n")

    moves_map = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }

    x, y = 0, 0
    for i, row in enumerate(board):
        if "@" in row:
            x = i
            y = row.index("@")
            break

    for move in moves:
        x += moves_map[move][0]
        y += moves_map[move][1]

        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return "crash"
        
        if board[x][y] == "*":
            return "success"

        if board[x][y] == "#":
            return "crash"
        
    return "fail"


def test(expected, received):
    return expected == received


def main():
    board = """
.....
.*#.*
.@...
.....
"""

    print(test("fail", moveReno(board, 'D')))
    # ➞ 'fail' -> se mueve pero no recoge nada

    print(test("success", moveReno(board, 'U')))
    # ➞ 'success' -> recoge algo (*) justo encima

    print(test("crash", moveReno(board, 'RU')))
    # ➞ 'crash' -> choca contra un obstáculo (#)

    print(test("success", moveReno(board, 'RRRUU')))
    # ➞ 'success' -> recoge algo (*)

    print(test("crash", moveReno(board, 'DD')))
    # ➞ 'crash' -> se choca con la parte de abajo del tablero

    print(test("success", moveReno(board, 'UUU')))
    # ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba

    print(test("fail", moveReno(board, 'RR')))
    # ➞ 'fail' -> se mueve pero no recoge nada


if __name__ =="__main__":
    main()