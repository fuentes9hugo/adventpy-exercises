"""Se han estropeado algunos trineos eléctricos y los elfos están buscando piezas de repuesto para arreglarlos, pero no tienen claro si las piezas que tienen sirven.

Las piezas de repuesto son cadenas de texto y el mecánico Elfon Masc ha dicho que una pieza de repuesto es válida si la pieza puede ser un palíndromo después de eliminar, como máximo, un carácter.

Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.

Nuestra función debe devolver un booleano que indique si la pieza de repuesto es válida o no con esa regla."""


def checkPart(part: str) -> bool:
    if part == part[::-1]: return True

    part_len = len(part)
    for i in range(part_len):
        aux_part = part[:i] + part[i+1:]
        if aux_part == aux_part[::-1]: return True
    
    return False



def test(e, r):
    return e == r


def main():
    print(test(True, checkPart("uwu"))) # true
    # "uwu" es un palíndromo sin eliminar ningún carácter

    print(test(True, checkPart("miidim"))) # true
    # "miidim" puede ser un palíndromo después de eliminar la primera "i"
    # ya que "midim" es un palíndromo

    print(test(False, checkPart("midu"))) # false
    # "midu" no puede ser un palíndromo después de eliminar un carácter


if __name__ == "__main__":
    main()