"""En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.

Dos árboles binarios son espejos si:

Las raíces de ambos árboles tienen el mismo valor.
Cada nodo del primer árbol debe tener su correspondiente nodo en la posición opuesta en el segundo árbol.
Y el árbol se representa con tres propiedades value, left y right. Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):

const tree = {
  value: '⭐️',
  left: {
    value: '🎅'
    // left: {...}
    // right: { ... }
  },
  right: {
    value: '🎁'
    // left: { ... }
    // right: { ...&nbsp;}
  }
}

Santa necesita tu ayuda para verificar si los árboles están sincronizados para que la estrella pueda seguir brillando. Debes devolver un array donde la primera posición indica si los árboles están sincronizados y la segunda posición devuelve el valor de la raíz del primer árbol."""


def isTreesSynchronized(tree1: dict, tree2: dict) -> list[bool, str]:
    if tree1["value"] != tree2["value"]:
        return [False, tree1["value"]]
    
    try:
        if tree1["right"]["value"] == tree2["left"]["value"] and tree1["left"]["value"] == tree2["right"]["value"]:
            return [True, tree1["value"]]
        
    except KeyError:
        return [True, tree1["value"]]

    return [False, tree1["value"]]


def main():
    tree1 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    tree2 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '⭐' },
    }

    print(isTreesSynchronized(tree1, tree2)) # [True, '🎄']

    r"""
    tree1          tree2
    🎄              🎄
    / \             / \
    ⭐   🎅         🎅   ⭐
    """

    tree3 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '🎁' }
    }

    print(isTreesSynchronized(tree1, tree3)) # [False, '🎄']

    tree4 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    print(isTreesSynchronized(tree1, tree4)) # [False, '🎄']

    print(isTreesSynchronized(
    { "value": '🎅' },
    { "value": '🧑‍🎄' }
    )) # [False, '🎅']

    print(isTreesSynchronized(
        { "value": "🎄" },
        { "value": "🎄" }
    )) # [True, "🎄"]

    print(isTreesSynchronized(
        { "value": '✨', "left": { "value": '⭐' }, "right": { "value": '🎅' } },
        { "value": '✨', "left": { "value": '🎅' }, "right": { "value": '🎁' } }
    )) # ["False", "✨"]

    print(isTreesSynchronized(
        { "value": "🎁" },
        { "value": "🎁" }
    )) # [True, "🎁"]

    print(isTreesSynchronized(
        { "value": "🎄" },
        { "value": "🎁" }
    )) # [False, "🎄"]

    print(isTreesSynchronized(
        { "value": '🎄', "left": { "value": '⭐' } },
        { "value": '🎄', "right": { "value": '⭐' } }
    )) # [True, "🎄"]

if __name__ == "__main__":
    main()