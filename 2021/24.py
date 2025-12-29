"""El abuelo 👴 dice que ve todos los árboles de navidad iguales... La abuela 👵, en cambio, piensa que no. Que todos los árboles de navidad son distintos...

Vamos a hacer una función que nos diga si dos árboles de navidad son iguales. Para ello, vamos a comparar los árboles que ya creamos en el reto 22.

Tenemos que ver si ambos árboles tienen la misma estructura y los mismos valores en todas las ramas. Aquí tienes unos ejemplos.

El cuñado 🦹‍♂️, que se las sabe todas, me ha dicho que tenga cuidado porque el truco del JSON.stringify puede no funcionar... ya que los árboles pueden ser el mismo pero el orden de representación de las ramas izquierda y derecha puede ser inversa..."""


def checkIsSameTree(treeA: dict, treeB: dict) -> bool:
    return treeA == treeB


def test(expected, received):
    return expected == received


def main():
    tree = {
    "value": 1,
    "left": { "value": 2, "left": None, "right": None },
    "right": { "value": 3, "left": None, "right": None }
    }

    print(test(True, checkIsSameTree(tree, tree))) # true

    tree2 = {
    "value": 1,
    "left": { "value": 3, "left": { "value": 2, "left": None, "right": None }, "right": None },
    "right": { "value": 5, "left": None, "right": { "value": 4, "left": None, "right": None } }
    }

    print(test(False, checkIsSameTree(tree, tree2))) # false
    print(test(True, checkIsSameTree(tree2, tree2))) # true

    tree3 = {
    "value": 1,
    "right": { "value": 3, "left": None, "right": None },
    "left": { "value": 2, "left": None, "right": None }
    }

    print(test(True, checkIsSameTree(tree, tree3))) # true


if __name__ == "__main__":
    main()