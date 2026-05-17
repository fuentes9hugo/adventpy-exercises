"""Estamos programando unos robots llamados giftbot 🤖🎁 que navegan de forma autónoma por los almacenes de regalos.

Estamos creando una función a la que le pasamos: el almacén 🏬 que deben navegar y los movimientos ↔️ que pueden realizar.

El almacén se representa como un array de cadenas de texto, donde:
- . significa que hay vía libre.
- * significa que hay un obstáculo.
- ! es la posición inicial del robot.

Los movimientos son un array de cadenas de texto, donde:
- R mueve al robot una posición a la derecha.
- L mueve al robot una posición a la izquierda.
- U mueve al robot una posición hacia arriba.
- D mueve al robot una posición hacia abajo.

Hay que tener en cuenta que el robot no puede superar los obstáculos ni los límites del almacén.

Dados un almacén y los movimientos, debemos devolver el array con la posición final de nuestro robot.

Ten en cuenta que la store es un array que puede ser de un número de filas que va de 1 a 100, ya que tenemos almacenes de todos los tamaños.

También que el robot es posible que termine en su posición inicial si no puede moverse o si está dando vueltas."""


def autonomousDrive(store: list[str], movements: list[str]) -> list[str]:
    store_len = len(store)
    row_len = len(store[0])

    movements_map = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    position_y, position_x = next((i, row.find("!")) for i, row in enumerate(store) if "!" in row)

    store_list = list(map(list, store))

    store_list[position_y][position_x] = "."

    for move in movements:
        move_y, move_x = movements_map[move]
        next_position_y = position_y + move_y
        next_position_x = position_x + move_x

        if not 0 <= next_position_y < store_len or not 0 <= next_position_x < row_len: continue

        if store_list[next_position_y][next_position_x] == "*": continue

        position_y = next_position_y
        position_x = next_position_x

    store_list[position_y][position_x] = "!"

    return ["".join(row) for row in store_list]


def test(e, r) -> bool:
    return e == r


def main():
    store = ['..!....', '...*.*.']

    movements = ['R', 'R', 'D', 'L']
    result = autonomousDrive(store, movements)
    print(test([".......", "...*!*."], result))
    print(result)
    """
    [
    ".......",
    "...*!*."
    ]
    """

    # El último movimiento es hacia la izquierda, pero no puede moverse porque hay un obstáculo.


if __name__ == "__main__":
    main()