"""¡Estamos haciendo los últimos ajustes para el trineo de Santa Claus!

Como ya sabes, el trineo es volador y estamos ajustando el motor para que haga parabolas lo más óptimas posibles. Para esto el salto debe ser siempre hacia arriba y, a partir del punto más alto, debe bajar siempre hacia abajo...

Nuestro mecánico de confianza, Kiko Belfs, que tiene un Tesla genial, nos ha explicado que los saltos se pueden ver como arrays... y que sólo tenemos que asegurarnos que los números suben y bajan de forma correcta. También nos avisa que sólo pasaremos arrays de, como mínimo, tres posiciones.

Nos ha pasado algunos ejemplos de cómo debería ser nuestra función y algunos resultados

Lo importante: recorrer el array de izquierda a derecha para ver que la subida es siempre estricta, detectar el punto más alto y entonces ver que la bajada es estricta hacia abajo..."""


def checkSledJump(heights: list[int]) -> bool:
    if len(heights) < 3: return False
    if heights[1] <= heights[0]: return False

    going_up = True
    prev_jump = heights[1]

    for jump in heights[2:]:
        if jump == prev_jump: return False

        if jump < prev_jump: going_up = False

        elif not going_up and jump > prev_jump: return False

        prev_jump = jump
    
    return not going_up


def test(expected, received):
    return expected == received


def main():
    print(test(True, checkSledJump([1, 2, 3, 2, 1]))) # true: sube y baja de forma estricta
    print(test(True, checkSledJump([0, 1, 0]))) # -> true: sube y baja de forma estricta
    print(test(True, checkSledJump([0, 3, 2, 1]))) # -> true: sube y baja de forma estricta
    print(test(True, checkSledJump([0, 1000, 1]))) # -> true: sube y baja de forma estrict
    print(test(False, checkSledJump([2, 4, 4, 6, 2]))) # false: no sube de forma estricta
    print(test(False, checkSledJump([1, 2, 3]))) # false: sólo sube
    print(test(False, checkSledJump([1, 2, 3, 2, 1, 2, 3]))) # false: sube y baja y sube... ¡no vale!
    print(test(False, checkSledJump([3, 2, 1]))) # -> false: no sube, solo baja
    print(test(False, checkSledJump([2, 2, 1]))) # -> false: no sube de forma estricta


if __name__ == "__main__":
    main()