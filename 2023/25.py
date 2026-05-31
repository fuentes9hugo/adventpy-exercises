"""Ya ha entregado Santa Claus 🎅 todos los regalos a los niños pero quieren revisar si pueden mejorar de cara al año que viene.

Los elfos quieren saber cuántos movimientos ha hecho Santa Claus 🛷 para entregar todos los regalos. Para ello, te dan un mapa de la ciudad con la ubicación de cada niño y de Santa.

El mapa es una cadena de texto multi línea donde cada caracter representa una casilla. Los niños se representan por números del 1 al 9 y Santa Claus por la letra S. El resto de casillas son .

Santa Claus sólo puede moverse hacia arriba, abajo, izquierda o derecha, y cada movimiento cuenta como 1 km. Además, siempre empieza en la posición S y debe entregar los regalos en orden, del 1 al 9.

Escribe una función travelDistance que reciba un mapa y devuelva la distancia total que ha recorrido Santa Claus según la posición de los niños.

Ten en cuenta que:
- El mapa no tiene por qué ser cuadrado.
- El mapa siempre tendrá al menos un niño.
- El mapa siempre tendrá una posición inicial para Santa Claus.
- Los números de los niños nunca se repiten."""


def travelDistance(map: str) -> int:
    map_list = map.split("\n")

    positions = {}

    for i, row in enumerate(map_list):
        for j, cell in enumerate(row):
            if cell != ".": positions[cell] = [i, j]
    
    current_pos = positions["S"]

    total_moves = 0

    for i in range(1, 10):
        kid = positions.get(str(i))

        if not kid: return total_moves

        total_moves += abs(current_pos[0] - kid[0]) + abs(current_pos[1] - kid[1])
        current_pos = kid
    
    return total_moves


def test(e, r) -> bool:
    return e == r


def main():
    map = """.....1....
..S.......
..........
....3.....
......2..."""

    result = travelDistance(map)
    print(result) # -> 12 km
    print(test(12, result)) # -> 12 km
    """
    De la S al niño 1: 4 movimientos
    Del niño 1 al 2: 5 movimientos
    Del niño 2 al 3: 3 movimientos
    Total: 12 movimientos
    """

    result2 = travelDistance("..S.1...")
    print(result2) # -> 2
    print(test(2, result2)) # -> 2


if __name__ == "__main__":
    main()