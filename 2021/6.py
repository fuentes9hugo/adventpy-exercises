"""Antes de poder disfrutar de la navidad... nos toca terminar de rematar los exámenes finales. ¡Y toca un poco de matemáticas! 😱

A una función se le pasan dos parámetros: un Array con números y el resultado que se espera.

La función debe devolver los dos valores del Array que sumen el resultado esperado. Como a veces pueden haber más de dos valores que sumen, se devolverá el primero empezando por la izquierda que encuentre otro par, sin importar lo lejos que esté a la derecha.

Si no se encuentra, se devuelve null.

El resultado tiene que ser un array con dos números.

Una vez que tengas el resultado... ¿cómo podrías hacer que fuese lo más óptimo posible para no tener que recorrer las mismas situaciones dos veces 🤔?"""


def sumPairs(numbers: list[int], result: int) -> tuple[int, int] | None:
    numbers_compared = []
    for i, number in enumerate(numbers, start=1):
        if i == len(numbers) or number in numbers_compared:
            continue
        complement = result - number
        if complement in numbers[i:]:
            return (number, complement)

        numbers_compared.append(number)
    
    return None


def test(expected, received):
    return expected == received


def main():
    print(test((3, 7), sumPairs([3, 5, 7, 2], 10))) # [3, 7]
    print(test(None, sumPairs([-3, -2, 7, -5], 10))) # None
    print(test((2, 2), sumPairs([2, 2, 3, 1], 4))) # [2, 2]
    print(test((6, 2), sumPairs([6, 7, 1, 2], 8))) # [6, 2]
    print(test((1, 5), sumPairs([0, 2, 2, 3, -1, 1, 5], 6))) # [1, 5]

if __name__ == "__main__":
    main()