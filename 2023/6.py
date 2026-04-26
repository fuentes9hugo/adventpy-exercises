"""Los elfos están catalogando los renos de Santa 🦌 según la distancia que pueden recorrer.

Para ello tienen una cadena de texto movements donde cada caracter representa la dirección del movimiento del reno:
- > = Avanza a la derecha
- < = Avanza a la izquierda
- * = Puede avanzar o retroceder

Por ejemplo, si el movimiento es >>*<, va hacia la derecha dos veces, luego puede ir a derecha o izquierda (lo que maximice la distancia recorrida final) y luego ir a la izquierda.

Los elfos quieren saber cuál es la máxima distancia que recorre el reno al finalizar todos los movimientos.

En el ejemplo anterior, la máxima distancia que recorre el reno es 2. Va a la derecha dos veces +2, luego con el * puede ir a la derecha otra vez para maximizar la distancia +1 y luego va a la izquierda -1.

Crea una función maxDistance que reciba la cadena de texto movements y devuelva la máxima distancia que puede recorrer el reno en cualquier dirección.

Ten en cuenta que no importa si es a la izquierda o la derecha, la distancia es el valor absoluto de la distancia recorrida máxima al finalizar los movimientos."""


def maxDistance(movements: str) -> int:
    movements_map = {
        ">": 1,
        "<": -1
    }

    result = 0

    wildcards = 0

    for movement in movements:
        if movement == "*":
            wildcards += 1
            continue
        
        result += movements_map[movement]

    return abs(result) + wildcards


def test(e, r) -> bool:
    return e == r


def main():
    movements = '>>*<'
    result = maxDistance(movements)
    print(test(2, result))
    print(result) # -> 2

    movements2 = '<<<>'
    result2 = maxDistance(movements2)
    print(test(2, result2))
    print(result2) # -> 2

    movements3 = '>***>'
    result3 = maxDistance(movements3)
    print(test(5, result3))
    print(result3) # -> 5


if __name__ == "__main__":
    main()