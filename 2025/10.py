"""🎄 Profundidad de Magia Navideña
En el Polo Norte, Santa Claus está revisando las cartas mágicas 📩✨ que recibe de los niños de todo el mundo. Estas cartas usan un antiguo lenguaje navideño en el que los corchetes [ y ] representan la intensidad del deseo.

Cuanto más profunda sea la anidación de los corchetes, más fuerte es el deseo. Tu misión es averiguar la máxima profundidad en la que se anidan los [].

Pero ¡cuidado! Algunas cartas pueden estar mal escritas. Si los corchetes no están correctamente balanceados (si se cierra antes de abrir, sobran cierres o faltan cierres), la carta es inválida y debes devolver -1."""


def maxDepth(s: str) -> int:
    depth = 0
    current_depth = 0
    for char in s:
        if char == "[":
            current_depth += 1

            if current_depth > depth:
                depth = current_depth
        else:
            current_depth -= 1

            if current_depth < 0:
                return -1

    return depth if current_depth == 0 else -1


def test(expected, receiveed):
    return expected == receiveed


def main():
    print(test(1, maxDepth('[]'))) # -> 1
    print(test(2, maxDepth('[[]]'))) # -> 2
    print(test(1, maxDepth('[][]'))) # -> 1
    print(test(2, maxDepth('[[][]]'))) # -> 2
    print(test(3, maxDepth('[[[]]]'))) # -> 3
    print(test(2, maxDepth('[][[]][]'))) # -> 2

    print(test(-1, maxDepth(']['))) # -> -1 (cierra antes de abrir)
    print(test(-1, maxDepth('[[['))) # -> -1 (faltan cierres)
    print(test(-1, maxDepth('[]]]'))) # -> -1 (sobran cierres)
    print(test(-1, maxDepth('[][]['))) # -> -1 (queda uno sin cerrar)


if __name__ == "__main__":
    main()