"""En el taller de Santa, los elfos están guardando regalos 🎁 en un almacén vertical. Los regalos se dejan caer uno a uno por una columna y se van apilando.

El almacén es una matriz con # regalos y . espacios vacíos. Debes crear una función dropGifts que reciba el estado del almacén y un array con las columnas donde se dejan caer los regalos.

Reglas de la caída:

- El regalo cae por la columna indicada desde arriba.
- Se coloca en la celda vacía (.) más baja de esa columna.
- Si la columna está llena, el regalo se ignora."""


def dropGifts(warehouse: list[list[str]], drops: list[int]) -> list[list[str]]:
    for drop in drops:
        for row in reversed(warehouse):
            if row[drop] == ".":
                row[drop] = "#"
                break

    return warehouse


def test(expected, received):
    return expected == received


def main():
    print(test([['.', '.', '.'], ['#', '#', '.'], ['#', '#', '.']],
        dropGifts(
        [
            ['.', '.', '.'],
            ['.', '#', '.'],
            ['#', '#', '.']
        ],
        [0])
    ))
    """
    [
    ['.', '.', '.'],
    ['#', '#', '.'],
    ['#', '#', '.']
    ]
    """

    print(test([['#', '.', '.'], ['#', '#', '#'], ['#', '#', '#']],
        dropGifts(
        [
            ['.', '.', '.'],
            ['#', '#', '.'],
            ['#', '#', '#']
        ],
        [0, 2])
    ))
    """
    [
    ['#', '.', '.'],
    ['#', '#', '#'],
    ['#', '#', '#']
    ]
    """

    print(test([['.', '.', '.'], ['.', '.', '.'],['#', '#', '#']],
        dropGifts(
        [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ],
        [0, 1, 2])
    ))
    """
    [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['#', '#', '#']
    ]
    """

    print(test([['#', '#'], ['#', '#']],
        dropGifts(
        [
            ['#', '#'],
            ['#', '#']
        ],
        [0, 0])
    ))
    """
    [
    ['#', '#'],S
    ['#', '#']
    ]
    """


if __name__ == "__main__":
    main()