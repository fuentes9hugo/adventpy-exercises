"""Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve mágica ❄️. Esta nieve tiene una propiedad especial: si dos montículos de nieve idénticos y adyacentes se encuentran, desaparecen automáticamente.

Tu tarea es escribir una función que ayude a los elfos a simular este proceso. El camino se representa por una cadena de texto y cada montículo de nieve un carácter.

Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales hasta que no queden más movimientos posibles.

El resultado debe ser el camino final después de haber eliminado todos los montículos duplicados:"""


def removeSnow(s: str) -> str:
    # if not s: return "" -> Sin esto funcionaría igual, pero está bien como early return
    no_snow = []
    for char in s:
        if no_snow and char == no_snow[-1]:
            no_snow.pop()
            continue

        no_snow.append(char)
    
    return "".join(no_snow)


def test(expected, received):
    return expected == received


def main():
    print(test("oz", removeSnow('zxxzoz'))) # -> "oz"
    # 1. Eliminamos "xx", quedando "zzoz"
    # 2. Eliminamos "zz", quedando "oz"

    print(test("abc", removeSnow('abcdd'))) # -> "abc"
    # 1. Eliminamos "dd", quedando "abc"

    print(test("z", removeSnow('zzz'))) # -> "z"
    # 1. Eliminamos "zz", quedando "z"

    print(test("a", removeSnow('a'))) # -> "a"
    # No hay montículos repetido


if __name__ == "__main__":
    main()