"""Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel a distribuir regalos dentro de un gran almacén. El robot se mueve en un plano 2D y partimos desde el origen (0, 0).

Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a estar justo donde empezó.

Las órdenes básicas del robot son:

L: Mover hacia la izquierda
R: Mover hacia la derecha
U: Mover hacia arriba
D: Mover hacia abajo
Pero también tiene ciertos modificadores para los movimientos:

*: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
!: El siguiente movimiento se invierte (ej: R!L se considera como RR)
?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R significa R)
Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento invertido y no el original. Por ejemplo, !U?U invierte el movimiento de U, por lo que contabiliza que se hizo el movimiento D pero no el U. Así !U?U se traduce como D?U y, por lo tanto, se haría el movimiento U final.

Debes devolver:

true: si el robot vuelve a estar justo donde empezó
[x, y]: si el robot no vuelve a estar justo donde empezó, devolver la posición donde se detuvo"""


def isRobotBack(moves: str) -> bool | list[int]:
    moves_map = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    multipliers = {
        "*": 2,
        "!": -1
    }

    position = [0, 0]
    current_multiplier = 1
    skip = False
    done_moves = set()
    for move in moves:
        if skip and move in done_moves:
            continue
        
        if move in multipliers:
            current_multiplier = multipliers[move]
            continue
        elif move == "?":
            skip = True
            continue
        
        position[0] += moves_map[move][0] * current_multiplier
        position[1] += moves_map[move][1] * current_multiplier

        if current_multiplier == -1:
            for key, value in moves_map.items():
                if value == (moves_map[move][0] * -1, moves_map[move][1] * -1):
                    done_moves.add(key)
                    break
        else:
            done_moves.add(move)

        current_multiplier = 1
        skip = False
        
    return position if position != [0, 0] else True


def test(expected, received):
    return expected == received


def main():
    print(test([1, 0], isRobotBack('R')))     # [1, 0]
    print(test(True, isRobotBack('RL')))    # true
    print(test(True, isRobotBack('RLUD')))  # true
    print(test([2, 1], isRobotBack('*RU')))   # [2, 1]
    print(test([1, 2], isRobotBack('R*U')))   # [1, 2]
    print(test([-4, 0], isRobotBack('LLL!R'))) # [-4, 0]
    print(test([1, 0], isRobotBack('R?R')))   # [1, 0]
    print(test(True, isRobotBack('U?D')))   # true
    print(test([2,0], isRobotBack('R!L')))   # [2,0]
    print(test([0,2], isRobotBack('U!D')))   # [0,2]
    print(test(True, isRobotBack('R?L')))   # true
    print(test([0,1], isRobotBack('U?U')))   # [0,1]
    print(test([0,2], isRobotBack('*U?U')))  # [0,2]
    print(test(True, isRobotBack('U?D?U'))) # true

    # Ejemplos paso a paso:
    print(test([1,0], isRobotBack('R!U?U'))) # [1,0]
    # 'R'  -> se mueve a la derecha 
    # '!U' -> se invierte y se convierte en 'D'
    # '?U' -> se mueve arriba, porque no se ha hecho el movimiento 'U'

    print(test([0,1], isRobotBack('UU!U?D'))) # [0,1]
    # 'U'  -> se mueve arriba
    # 'U'  -> se mueve arriba
    # '!U' -> se invierte y se convierte en 'D'
    # '?D' -> no se mueve, ya que ya se hizo el movimiento 'D'


if __name__ == "__main__":
    main()