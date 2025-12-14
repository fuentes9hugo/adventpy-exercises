"""El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.

Nota: ¿Quieres una pista? Seguro que has jugado al juego de buscaminas antes… 😉"""


def detectBombs(grid: list[list[bool]]) -> list[list[int]]:
    bombs_detected = []
    neighbor_bombs = tuple((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y)
    for i, row in enumerate(grid):
        bomb_x = i
        row_to_append = []
        for j in range(len(row)):
            bomb_y = j
            bombs_num = 0
            for x, y in neighbor_bombs:
                if len(grid) > bomb_x + x >= 0 and len(row) > bomb_y + y >= 0:
                    if grid[bomb_x + x][bomb_y + y]:
                        bombs_num += 1
                
            row_to_append.append(bombs_num)
        
        bombs_detected.append(row_to_append)

    return bombs_detected


def test(expected, received):
    return expected == received


def main():
    print(test([[1, 2, 1], [2, 1, 1], [1, 1, 1]], detectBombs([
        [True, False, False],
        [False, True, False],
        [False, False, False]
    ])))
    # [
    #   [1, 2, 1],
    #   [2, 1, 1],
    #   [1, 1, 1]
    # ]

    print(test([[0, 1], [1, 1]], detectBombs([
        [True, False],
        [False, False]
    ])))
    # [
    #   [0, 1],
    #   [1, 1]
    # ]

    print(test([[1, 1], [4, 4], [1, 1]], detectBombs([
        [True, True],
        [False, False],
        [True, True]
    ])))

    # [
    #   [1, 1],
    #   [4, 4],
    #   [1, 1]
    # ]


if __name__ == "__main__":
    main()