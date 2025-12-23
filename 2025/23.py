"""Papá Noel 🎅 tiene que repartir regalos en un pueblo representado como un mapa en cuadrícula.

Cada celda del mapa puede ser:

'S' → Punto de partida de Papá Noel
'G' → Casa que debe recibir un regalo
'.' → Camino libre
'#' → Obstáculo (no se puede pasar)
Papá Noel realiza entregas independientes para cada regalo. Sale de 'S', entrega el regalo en una casa 'G' y vuelve inmediatamente a 'S' para recoger el siguiente. Sin embargo, para este reto, solo queremos calcular la suma de las distancias mínimas de ida desde 'S' hasta cada casa 'G'.

Tu tarea

Escribe la función minStepsToDeliver(map) que devuelva el número total de pasos necesarios para llegar a todas las casas con regalos desde la posición inicial.

Ten en cuenta:

- Siempre se parte de la posición inicial 'S'.
- Para cada regalo, calcula la distancia mínima desde 'S' hasta esa casa 'G'.
- No puedes atravesar obstáculos ('#').
- Si alguna casa con regalo es inalcanzable, la función debe devolver -1.

Reglas

- El mapa siempre contiene exactamente una 'S'.
- Puede haber 0 o más casas con regalos ('G').
- No importa el orden de las entregas, ya que cada una se mide de forma independiente desde 'S'.
- Debes devolver la suma de las distancias mínimas de ida.

Pista

- Calcula la distancia más corta desde 'S' hasta cada 'G' (puedes usar un algoritmo de búsqueda en anchura o BFS).
- Si algún regalo no tiene camino posible, el resultado total es -1."""


def minStepsToDeliver(map: list[list[str]]) -> int:
    moves_map = ((0, 1), (1, 0), (0, -1), (-1, 0))

    current_pos = ()
    houses_ammount = 0
    for i, row in enumerate(map):
        if "S" in row: current_pos = (i, row.index("S"))

        houses_ammount += row.count("G")

    if houses_ammount == 0: return -1

    traveled_houses = set()
    visited_pos = {current_pos}

    from collections import deque

    queue = deque([(current_pos, 0)])

    steps_ammount = 0

    while queue:
        current_pos, steps = queue.popleft()
        
        for move in moves_map:
            next_y = current_pos[0] + move[0]
            next_x = current_pos[1] + move[1]
            current_steps = steps

            if not 0 <= next_y < len(map) or not 0 <= next_x < len(map[0]): continue

            next_move = (next_y, next_x)
            current_steps += 1

            if map[next_y][next_x] == "#" or next_move in visited_pos: continue

            if map[next_y][next_x] == "G" and next_move not in traveled_houses:
                steps_ammount += current_steps
                traveled_houses.add(next_move)

                if len(traveled_houses) == houses_ammount: return steps_ammount

                queue.append((next_move, current_steps))
            
            elif map[next_y][next_x] == ".":
                queue.append((next_move, current_steps))
            
            visited_pos.add(next_move)
    
    return -1


def test(expected, received):
    return expected == received


def main():
    print(test(4, minStepsToDeliver([
        ['S', '.', 'G'],
        ['.', '#', '.'],
        ['G', '.', '.']
    ])))
    # Resultado: 4

    """ 
    Explicación:
    - Distancia mínima de S (0,0) a G (0,2): 2 pasos
    - Distancia mínima de S (0,0) a G (2,0): 2 pasos
    - Total: 2 + 2 = 4
    """

    print(test(-1, minStepsToDeliver([
        ['S', '#', 'G'],
        ['#', '#', '.'],
        ['G', '.', '.']
    ])))
    # Resultado: -1
    # (La casa en (0,2) es inalcanzable por los obstáculos)

    print(test(1, minStepsToDeliver([['S', 'G']])))
    # Resultado: 1

    print(test(21, minStepsToDeliver([['S', 'G', 'G', 'G', 'G', 'G', 'G']])))
    # Resultado: 21

    print(test(47, minStepsToDeliver([
        ['S', '.', 'G', '.', '.', '.'],
        ['#', '#', '#', '.', '#', '.'],
        ['G', '.', '.', '.', '#', 'G'],
        ['G', '.', '.', '#', '#', '#'],
        ['G', '.', '.', '#', '#', '#'],
        ['G', '.', '.', '#', '#', '#']
    ])))

    print(test(3, minStepsToDeliver([['S', '.', '.', 'G']])))

    print(test(-1, minStepsToDeliver([['S', '.', '.', 'G', '.', '#', 'G']])))

    print(test(34, minStepsToDeliver([
        ['S', '.', 'G', 'G', '.', '.'],
        ['.', '#', '.', '#', '#', '.'],
        ['.', '#', '.', '#', '.', 'G'],
        ['.', '.', 'G', '#', '.', '#'],
        ['.', '.', '#', '#', '.', '#'],
        ['.', 'G', '.', '#', 'G', '#']
    ])))

if __name__ == "__main__":
    main()