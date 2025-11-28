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