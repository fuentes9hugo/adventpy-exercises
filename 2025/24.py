"""
En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo, para que funcionen correctamente, los árboles deben estar en perfecta sincronía como espejos 🪞.

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
    def check_mirror(node1, node2):
        if not node1 and not node2:
            return True
        
        if not node1 or not node2:
            return False
        
        if node1.get('value') != node2.get('value'):
            return False
            
        return (check_mirror(node1.get('left'), node2.get('right')) and
                check_mirror(node1.get('right'), node2.get('left')))

    is_sync = check_mirror(tree1, tree2)
    
    return [is_sync, tree1.get('value')]


def test(expected, received):
    return expected == received


def main():
    tree1 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    tree2 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '⭐' }
    }

    print(test([True, '🎄'], isTreesSynchronized(tree1, tree2))) # [true, '🎄']

    r"""
    tree1          tree2
    🎄              🎄
    / \             / \
   ⭐ 🎅          🎅  ⭐
    """

    tree3 = {
        "value": '🎄',
        "left": { "value": '🎅' },
        "right": { "value": '🎁' }
    }

    print(test([False, '🎄'], isTreesSynchronized(tree1, tree3))) # [false, '🎄']

    tree4 = {
        "value": '🎄',
        "left": { "value": '⭐' },
        "right": { "value": '🎅' }
    }

    print(test([False, '🎄'], isTreesSynchronized(tree1, tree4))) # [false, '🎄']

    print(test([False, '🎅'], isTreesSynchronized(
        { "value": '🎅' },
        { "value": '🧑‍🎄' }
    ))) # [false, '🎅']


if __name__ == "__main__":
    main()