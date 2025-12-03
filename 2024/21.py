"""Santa Claus 🎅 está decorando un árbol de Navidad mágico 🪄, que este año tiene una estructura especial en forma de árbol binario. Cada nodo del árbol representa un regalo, y Santa quiere saber la altura del árbol para colocar la estrella mágica en la punta.

Tu tarea es escribir una función que calcule la altura de un árbol binario. La altura de un árbol binario se define como el número máximo de niveles desde la raíz hasta una hoja. Un árbol vacío tiene una altura de 0."""


def treeHeight(tree: dict) -> int:
    return 1 + max(treeHeight(tree["left"]), treeHeight(tree["right"])) if tree else 0


# Generic function to solve the problem if the tree is not binary and has more branches
"""def treeHeight(tree: dict) -> int:
    if not tree:
        return 0

    sides_height = []
    for side in tree.keys():
        if side != "value":
            sides_height.append(treeHeight(tree[side]))
    
    return 1 + max(sides_height)"""

def main():
    # Definición del árbol
    tree = {
    "value": '🎁',
    "left": {
        "value": '🎄',
        "left": {
        "value": '⭐',
        "left": None,
        "right": None
        },
        "right": {
        "value": '🎅',
        "left": None,
        "right": None
        }
    },
    "right": {
        "value": '❄️',
        "left": None,
        "right": {
        "value": '🦌',
        "left": None,
        "right": None
        }
    }
    }

    # Representación gráfica del árbol:
    #        🎁
    #       /   \
    #     🎄     ❄️
    #    /  \      \
    #  ⭐   🎅      🦌

    # Llamada a la función
    print(treeHeight(tree))
    # Devuelve: 3
    
    print(treeHeight({
        "value": '🎁',
        "left": None,
        "right": None
        }))
    # Devuelve: 1

    print(treeHeight({
        "value": '🎁',
        "left": {
            "value": '🎄',
            "left": None,
            "right": None
        },
        "right": {
            "value": '❄️',
            "left": None,
            "right": None
        }
        }))
    # Devuelve: 2

    print(treeHeight({
        "value": '🎁',
        "left": {
            "value": '🎄',
            "left": {
            "value": '⭐',
            "left": None,
            "right": None
            },
            "right": None
        },
        "right": {
            "value": '❄️',
            "left": None,
            "right": None
        }
        }))
    # Devuelve: 3

    print(treeHeight(None))
    # Devuelve: 0

    print(treeHeight({
        "value": '🎁',
        "left": {
            "value": '🎄',
            "left": {
            "value": '⭐',
            "left": {
                "value": '🎅',
                "left": None,
                "right": None
            },
            "right": None
            },
            "right": None
        },
        "right": None
        }))
    # Devuelve: 4


if __name__ == "__main__":
    main()