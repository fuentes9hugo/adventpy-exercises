"""Papá Noel 🎅 está probando un nuevo simulador de trineo dentro de un laberinto en el taller. El laberinto se representa como una matriz de caracteres.

Tu tarea es implementar una función que determine si es posible llegar a la salida (E) partiendo desde la posición inicial (S).

Reglas del laberinto:

- S: Posición inicial de Santa.
- E: Salida del laberinto.
- .: Camino libre.
- #: Pared (bloquea el paso).
- Movimientos permitidos: arriba, abajo, izquierda y derecha.
- Solo hay una S y una sola E.

A tener en cuenta:

- No necesitas devolver el camino, solo si es posible llegar.
- Santa no puede salir de los límites del laberinto.
Consejo: Este problema se puede resolver de varias formas, pero algoritmos de búsqueda como BFS (búsqueda en anchura) o DFS (búsqueda en profundidad) son ideales para este tipo de retos."""


# Solución utilizando búsqueda de profundidad (DFS). No es lo más óptimo para encontrar el camino más rápido
# Este tipo de algoritmos funciona bien para encontrar todos los caminos
"""def canEscape(maze: list[list[str]]) -> bool:
    moves_map = ((0, 1), (1, 0), (0, -1), (-1, 0))
    current_position = next((i, row.index("S")) for i, row in enumerate(maze) if "S" in row)

    traveled_positions = {current_position}

    def check_next_moves(maze: list[list[str]], current_position: tuple[int, int], traveled_positions: set) -> bool:
        next_moves = []
        for move in moves_map:
            next_position_y = current_position[0] + move[0]
            next_position_x = current_position[1] + move[1]

            if not 0 <= next_position_y < len(maze) or not 0 <= next_position_x < len(maze[0]) or (next_position_y, next_position_x) in traveled_positions: continue
            
            if maze[next_position_y][next_position_x] == ".":
                next_moves.append((next_position_y, next_position_x))
            
            elif maze[next_position_y][next_position_x] == "E":
                return True
        
        for move in next_moves:
            traveled_positions.add(move)
            if check_next_moves(maze, move, traveled_positions): return True
        
        return False
        
    return check_next_moves(maze, current_position, traveled_positions)"""


# Solución utilizando búsqueda en anchua (BFS). Este sí que es el más óptimo para este tipo de problemas
# Este tipo de algoritmos funciona bien para encontrar el camino más rápido
# Deque es un lista optimizada para poder modificarla tanto desde el principio como del final, como en este caso que usamos una pila FIFO
def canEscape(maze: list[list[str]]) -> bool:
    moves_map = ((0, 1), (1, 0), (0, -1), (-1, 0))
    current_position = next((i, row.index("S")) for i, row in enumerate(maze) if "S" in row)

    traveled_positions = {current_position}

    from collections import deque

    queue = deque([current_position])

    while queue:
        current_position_y, current_position_x = queue.popleft()

        for move in moves_map:
            next_position_y = current_position_y + move[0]
            next_position_x = current_position_x + move[1]

            if not 0 <= next_position_y < len(maze) or not 0 <= next_position_x < len(maze[0]) or (next_position_y, next_position_x) in traveled_positions: continue
        
            if maze[next_position_y][next_position_x] == "E": return True
        
            if maze[next_position_y][next_position_x] == ".":
                traveled_positions.add((next_position_y, next_position_x))
                queue.append((next_position_y, next_position_x))
        
    return False


def test(expected, received):
    return expected == received


def main():
    print(test(True, canEscape([
        ['S', '.', '#', '.'],
        ['#', '.', '#', '.'],
        ['.', '.', '.', '.'],
        ['#', '#', '#', 'E']
    ])))
    # → true

    print(test(False, canEscape([
        ['S', '#', '#'],
        ['.', '#', '.'],
        ['.', '#', 'E']
    ])))
    # → false

    print(test(True, canEscape([['S', 'E']])))
    # → true

    print(test(True, canEscape([
        ['S', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', 'E']
    ])))
    # → true

    print(test(False, canEscape([
        ['S', '.', '.'],
        ['.', '.', '.'],
        ['#', '#', '#'],
        ['.', '.', 'E']
    ])))
    # → false


if __name__ == "__main__":
    main()