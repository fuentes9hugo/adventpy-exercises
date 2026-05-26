"""¡Tenemos problemas con la carga de los juguetes en el trineo 🛷 de Santa 🎅! Parece que la distribución de los juguetes no es la adecuada y el trineo no puede despegar. ¿Podrías ayudarnos a resolver este problema?

Para solucionarlo hemos decidido utilizar un método similar al de un filtro de imágenes. En cada posición, vamos a distribuir la carga de los juguetes en función del número de juguetes de las posiciones vecinas.

Una posición vecina es aquella que está encima, abajo, a la izquierda o a la derecha de la posición actual. Por lo tanto, no se consideran vecinas las posiciones en diagonal.

Escribe una función distributeGifts que reciba una matriz de números representando los juguetes en el trineo y devuelva otra matriz con el mismo tamaño y número de elementos pero donde cada elemento es el promedio de su valor original y los valores de sus vecinos.

Ten en cuenta que hay posiciones que son null y que no contarán para el promedio como vecino pero sí se sustituirá por el valor promedio de sus vecinos.

Por ejemplo, vamos a ver un ejemplo completo.

Ten en cuenta:
- Las matrices no siempre son cuadradas, pueden tener más filas que columnas o viceversa.
- Para redondear los valores, debes utilizar la función Math.round() de JavaScript.
- Los valores null no se tienen en cuenta para el cálculo del promedio pero sí se sustituyen por el valor promedio de sus vecinos.
- Los bordes de la matriz tienen menos vecinos posibles que el resto de posiciones.
- Siempre son números enteros positivos."""


def distributeGifts(weights: list[list[int | None]]) -> list[list[int | None]]:
    neighbors = tuple((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i not in (j, -j))

    def cell_average(num: int | None, x: int, y: int) -> int:
        num_counter = 0 if num is None else 1
        avg = 0 if num is None else num

        for i, j in neighbors:
            check_x = x + i
            check_y = y + j

            if not 0 <= check_x < len(weights) or not 0 <= check_y < len(weights[0]): continue
            
            cell = weights[check_x][check_y]

            if cell is None: continue

            avg += cell
            num_counter += 1

        return round(avg / num_counter)

    return [[cell_average(cell, i, j) for j, cell in enumerate(row)] for i, row in enumerate(weights)]


def test(e, r) -> bool:
    return e == r


def main():
    input = [
        [4, 5, 1],
        [6, None, 3],
        [8, None, 4]
    ]

    for row in distributeGifts(input):
        print(row)

    print(test(
        [
            [5, 3, 3],
            [6, 5, 3],
            [7, 6, 4]
         ], distributeGifts(input)))

    # Resultado paso a paso de los primeros cálculos:

    # En la posición [0][0] tenemos el valor 4
    # Sus vecinos son los valores 5 y 6
    # (4 + 5 + 6) / 3 = 5

    # En la posición [0][1] tenemos el valor 5
    # Sus vecinos son los valores 4 y 1
    # (5 + 4 + 1) / 3 = 3.33
    # Math.round(3.33) = 3

    # En la posición [0][2] tenemos el valor 1
    # Sus vecinos son los valores 5 y 3
    # (1 + 5 + 3) / 3 = 3

    # En la posición [1][0] tenemos el valor 6
    # Sus vecinos son los valores 4, 8
    # (6 + 4 + 8 ) / 3 = 6

    # En la posición [1][1] tenemos el valor null
    # Sus vecinos son los valores 5, 6 y 3
    # (5 + 6 + 3) / 3 = 4.66
    # Math.round(4.66) = 5
    # ... y así con el resto de posiciones
    # [
    #     [(4 + 5 + 6) / 3, (5 + 4 + 1) / 3, (1 + 5 + 3) / 3],
    #     [(6 + 4 + 8) / 3, (5 + 6 + 3) / 3, (3 + 1 + 4) / 3],
    #     [(8 + 6) / 2, (8 + 4) / 2, (4 + 3) / 2]
    # ]

    # Resultado final tras redondear con Math.round()
    # [
    #     [5, 3, 3],
    #     [6, 5, 3],
    #     [7, 6, 4]
    # ]


if __name__ == "__main__":
    main()