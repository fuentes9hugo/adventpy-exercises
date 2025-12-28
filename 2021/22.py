"""¡Ay! Que llega la Navidad y no hemos decorado todavía el árbol. 🎄😱

Necesitamos una función que pasándole un árbol binario nos diga el número de decoraciones que necesitamos. Para ello tenemos un objeto que sería la representación del árbol y que nos indica en cada nivel el número de ramas a decorar.

Lo mejor es que veamos un ejemplo.

Por cierto, Bellf Gates me ha contado que este tipo de ejercicio es muy típico en las entrevistas de trabajo para programadores. ¿Lo sabías?"""


def countDecorations(bigTree: dict) -> int:
    return bigTree["value"] + countDecorations(bigTree["left"]) + countDecorations(bigTree["right"]) if bigTree else 0


def test(expected, received):
    return expected == received


def main():
    # tenemos el árbol en forma de objeto
    tree = {
    "value": 1, # el nodo raíz siempre es uno, porque es la estrella ⭐
    "left": {
        "value": 2, # el nodo izquierdo necesita dos decoraciones
        "left": None, # no tiene más ramas
        "right": None # no tiene más ramas
    },
    "right": {
        "value": 3, # el nodo de la derecha necesita tres decoraciones
        "left": None, # no tiene más ramas
        "right": None # no tiene más ramas
    }
    }

    """ Gráficamente sería así:
        1
    /   \
    2     3

    1 + 2 + 3 = 6
    """

    print(test(6, countDecorations(tree))) # 6

    bigTree = {
    "value": 1,
    "left": {
        "value": 5,
        "left": {
        "value": 7,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": None
        },
        "right": None
    },
    "right": {
        "value": 6,
        "left": {
        "value": 5,
        "left": None,
        "right": None
        },
        "right": {
        "value": 1,
        "left": None,
        "right": None
        }
    }
    }

    """
            1
        /   \
        5     6
        /     / \
    7     5   1
    /
    3
    """

    print(test(28, countDecorations(bigTree))) # 28


if __name__ == "__main__":
    main()