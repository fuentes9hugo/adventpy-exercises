"""Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este tren se mueve en un tablero representado por un array de strings.

El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue las siguientes reglas:

Recibirás dos parámetros board y mov.

board es un array de strings que representa el tablero:

@ es la locomotora del tren.
o son los vagones del tren.
* es una fruta mágica.
· son espacios vacíos.
mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:

'L': izquierda
'R': derecha
'U': arriba
'D': abajo.
Con esta información, debes devolver una cadena de texto:

'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
'eat': Si el tren recoge una fruta mágica (*).
'none': Si avanza sin chocar ni recoger ninguna fruta mágica."""


from typing import List, Literal


def test(expected, received):
    if expected == received:
        return True

    return False


def moveTrain(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    move_map = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1)
    }

    head_x = head_y = 0
    for x, row in enumerate(board):
        y = row.find("@")

        if y != -1:
            head_x, head_y = x, y
            break

    head_x += move_map[mov][0]
    head_y += move_map[mov][1]

    if any(i < 0 for i in (head_x, head_y)) or any([head_x >= len(board), head_y >= len(board[0])]):
        return "crash"
    
    move = board[head_x][head_y]

    if move == "o":
        return "crash"

    elif move == "*":
        return "eat"
    
    return 'none'


def main():
    board = [
        '·····',
        '*····',
        '@····',
        'o····',
        'o····'
    ]

    print(test("eat", moveTrain(board, 'U')))
    # Porque el tren se mueve hacia arriba y encuentra una fruta mágica

    print(test("crash", moveTrain(board, 'D')))
    # El tren se mueve hacia abajo y la cabeza se choca consigo mismo

    print(test("crash", moveTrain(board, 'L')))
    # El tren se mueve a la izquierda y se choca contra la pared

    print(test("none", moveTrain(board, 'R')))
    # El tren se mueve hacia derecha y hay un espacio vacío en la derecha

    print(test("eat", moveTrain([
        "·····",
        "··*··",
        "··@··",
        "··o··",
        "··o··"
    ], 'U')))

    print(test("crash", moveTrain([
        "·····",
        "··*··",
        "··.··",
        "··o··",
        "··@··"
    ], 'D')))

    print(test("crash", moveTrain([
        "·····",
        "··*··",
        "··@··",
        "··o··",
        "··o··"
    ], 'D')))

    print(test("none", moveTrain([
        "·····",
        "··*··",
        "··@··",
        "··o··",
        "··o··"
    ], 'R')))

    print(test("crash", moveTrain([
        "··@··",
        "··o··",
        "·*o··",
        "··o··",
        "··o··"
    ], 'U')))

    print(test("none", moveTrain([
        "··@··",
        "··o··",
        "·*o··",
        "··o··",
        "··o··"
    ], 'L')))

    print(test("eat", moveTrain([
        "·····",
        "··@··",
        "··*··",
        "·····",
        "·····"
    ], 'D')))


if __name__ =="__main__":
    main()