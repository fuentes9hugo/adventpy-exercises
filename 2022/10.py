"""Crea un programa que compruebe que el trineo de Santa Claus hace una parabola al saltar entre ciudades. Recibes un array de números que representan la altura en la que se encuentra el trineo en cada momento.

Para que la parabola sea correcta, el viaje del trineo debe ser ascendente al principio, llegar al punto más alto y descender hasta el final. No puede volver a subir una vez que ha bajado, ni puede iniciar el viaje bajando.

Necesitamos que el programa devuelva un boolean que indique si el trineo hace una parabola o no.

A tener en cuenta
- Para que el salto sea válido tiene que subir una vez y bajar una vez. Si durante el salto se queda en la misma altura entre dos posiciones, la parabola continua.
- No hace falta que el punto de inicio y final sean el mismo (las ciudades pueden estar a diferentes alturas)."""


def checkJump(heights: list[int]) -> bool:
    max_num = max(heights)
    max_num_index = next(len(heights) - 1 - i for i, height in enumerate(reversed(heights)) if height == max_num)

    up, down = heights[:max_num_index + 1], heights[max_num_index + 1:]

    return len(up) > 1 and bool(down) and all(height <= up[i + 1] for i, height in enumerate(up) if i < len(up) - 1) and all(height >= down[i + 1] for i, height in enumerate(down) if i < len(down) - 1)


def test(e, r):
    return e == r


def main():
    heights = [1, 3, 8, 5, 2]
    print(test(True, checkJump(heights))) # true

    
    # Es `true`.
    # El salto va de abajo a arriba y luego de arriba a abajo:
    """
        8 (punto más alto)
       ↗ ↘
      3   5
     ↗     ↘
    1        2
    """

    heights = [1, 7, 3, 5]
    print(test(False, checkJump(heights))) # false

    
    # Es `false`.
    # Va de abajo a arriba, de arriba a abajo y luego sube otra vez.
    """
       7   5 
     ↗ ↘ ↗
    1    3
    """

    heights = [1, 1, 6, 6, 5, 3, 3, 2]
    print(test(True, checkJump(heights))) # true

    heights = [7, 5, 3]
    print(test(False, checkJump(heights))) # false

    heights = [1, 2, 4, 7]
    print(test(False, checkJump(heights))) # false


if __name__ == "__main__":
    main()