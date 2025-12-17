"""En el taller de Santa 🎅 se están preparando los trineos de motor eléctrico para poder hacer la ruta perfecta para dejar los regalos.

La ruta empieza en el punto 0 y de ahí va hacia la derecha en línea recta.

El Keanu Relfes 🧝 nos ha preparado una lista de obstáculos a evitar. El problema es que nos ha dado la lista de posiciones de los obstáculos desordenada... 😅 aunque al menos nunca la posición 0 puede tener un obstáculo.

Encima, el trineo sólo se puede configurar para saltar un número fijo de posiciones... 😱

Necesitamos una función que nos diga la longitud mínima del salto del trineo para ir evitando todos los obstáculos en la ruta.

La dificultad del reto está en pensar que sólo podemos configurar el salto del trineo una vez y que buscamos el salto mínimo que nos serviría para sortear todos los obstaculos."""


def getMinJump(obstacles: list[int]) -> int:
    obstacles = set(obstacles)
    max_obstacle = max(obstacles)
    not_obstacles = (place for place in range(2, max_obstacle) if place not in obstacles)
    for jump in not_obstacles:
        all_jumps = jump
        obstacle_found = False
        for _ in range(max_obstacle // jump):
            if all_jumps in obstacles:
                obstacle_found = True
                break

            all_jumps += jump

        if not obstacle_found: return jump
    
    return max_obstacle + 1


def test(expected, received):
    return expected == received


def main():
    obstacles = [5, 3, 6, 7, 9]
    print(test(4, getMinJump(obstacles))) # -> 4

    # S es salto, X es obstáculo
    """Así quedaría la representación:
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    .  .  .  X  .  X  X  X  .  X  . 
    S-----------S-----------S-------
    """

    obstacles = [2, 4, 6, 8, 10]
    print(test(7, getMinJump(obstacles))) # -> 7

    """Así quedaría la representación:
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    .  .  X  .  X  .  X  .  X  .  X 
    S--------------------S---------
    """

    # Longitudes de salto:
    # 1 caería en el 2
    # 2 caería en el 2
    # 3 caería en el 6
    # 4 caería en el 4
    # 5 caería en el 10
    # 6 caería en el 6
    # 7 es el ideal!!! ✅

    print(test(4, getMinJump([1, 2, 3, 5]))) # -> 4
    print(test(2, getMinJump([3, 7, 5]))) # -> 2
    print(test(2, getMinJump([9, 5, 1]))) # -> 2


if __name__ == "__main__":
    main()