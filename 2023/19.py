"""¡Alerta en la fábrica de juguetes de Santa! El Grinch 😈 se ha infiltrado en el almacén y ha saboteado algunos de los juguetes 💣.

Los elfos necesitan ayuda para encontrar los juguetes saboteados y eliminarlos antes de que llegue la Navidad. Para ello tenemos el mapa 🗺️ del almacén, que es una matriz.

Los * representan los juguetes saboteados y las celdas vacías con un espacio en blanco son los lugares seguros.

Tu tarea es escribir una función que devuelva la misma matriz pero, en cada posición, nos indique el número de juguetes saboteados que hay en las celdas adyacentes.

Si una celda contiene un juguete saboteado, debe permanecer igual. Si una celda no toca ningún juguete saboteado, debe contener un espacio en blanco.

Ten en cuenta que…
- Las celdas diagonales también se consideran adyacentes.
- El tablero siempre tendrá al menos una celda vacía y un juguete saboteado *.
- El tablero puede tener cualquier tamaño.
- Los números son cadenas de texto."""


def revealSabotage(store: list[list[str]]) -> list[list[str]]:
    neighbor_cells = set((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))

    def bombs_conuter(x: int, y: int) -> str:
        bombs = 0
        
        for i, j in neighbor_cells:
            check_x = x + i
            check_y = y + j

            if not 0 <= check_x < len(store) or not 0 <= check_y < len(store[0]):
                continue
                
            if store[check_x][check_y] == "*": bombs += 1

        return str(bombs) if bombs != 0 else " "
    
    return [[bombs_conuter(i, j) if cell == " " else "*" for j, cell in enumerate(row)] for i, row in enumerate(store)]


def test(e, r) -> bool:
    return e == r


def main():
    store = [
        ['*', ' ', ' ', ' '],
        [' ', ' ', '*', ' '],
        [' ', ' ', ' ', ' '],
        ['*', ' ', ' ', ' ']
    ]

    for row in revealSabotage(store):
        print(row)

    """ Debería mostrar:
    [
        ['*', '2', '1', '1'],
        ['1', '2', '*', '1'],
        ['1', '2', '1', '1'],
        ['*', '1', ' ', ' ']
    ]
    """

    print(test(
        [
            ['*', '2', '1', '1'],
            ['1', '2', '*', '1'],
            ['1', '2', '1', '1'],
            ['*', '1', ' ', ' ']
        ], revealSabotage(store)))


if __name__ == "__main__":
    main()