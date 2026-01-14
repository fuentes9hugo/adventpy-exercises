"""En los almacenes de Papá Noel están haciendo inventario. Hay tres almacenes (que se representa cada uno como un Array). En cada almacén hay regalos.

Nos han pedido que escribamos un programa que nos diga qué regalos hay que comprar para reponer en nuestros almacenes ahora que se acerca la Navidad. Un regalo se tiene que reponer cuando sólo hay stock en uno de los tres almacenes.

Por ejemplo, si tenemos los siguientes almacenes:

const a1 = ['bici', 'coche', 'bici', 'bici']
const a2 = ['coche', 'bici', 'muñeca', 'coche']
const a3 = ['bici', 'pc', 'pc']

/* El almacén a1 tiene "bici" y "coche".
El almacén a2 tiene "coche", "bici" y "muñeca".
El almacén a3 tiene "bici" y "pc".

El regalo "muñeca" y "pc" sólo están en los almacenes a2 y a3 respectivamente.
*/

const gifts = getGiftsToRefill(a1, a2, a3) // ['muñeca', 'pc']
Como ves, los almacenes pueden tener el mismo regalo repetido varias veces. Pero, por más existencias que haya en un almacén, si no tenemos en los otros dos, debemos reponerlo para tener mejor distribución.

📝 Summary
- Crea una función getGiftsToRefill que reciba tres Array como parámetros.
- La función debe devolver un Array con los regalos que hay que reponer.
- Un regalo se debe reponer cuando sólo hay stock en uno de los tres almacenes.
- Si no hay ningún regalo que reponer, la función debe devolver un Array vacío.
- Si hay más de un regalo que reponer, la función debe devolver un Array con todos los regalos que hay que reponer."""


def getGiftsToRefill(a1: list[str], a2: list[str], a3: list[str]) -> list[str]:
    s1, s2, s3 = frozenset(a1), frozenset(a2), frozenset(a3)
    gifts = {gift: 0 for gift in s1 | s2 | s3} # "|" unión de conjuntos
    for gift in gifts.keys():
        for warehouse in (s1, s2, s3):
            if gift in warehouse: gifts[gift] += 1 # Hemos convertido los 3 almacenes en sets porque es más eficiente buscar en sets que en listas

    return [gift for gift, num_wh in gifts.items() if num_wh == 1]

"""
def getGiftsToRefill(a1: list[str], a2: list[str], a3: list[str]) -> list[str]:
    s1, s2, s3 = frozenset(a1), frozenset(a2), frozenset(a3)
    unique_gifts = (s1 - s2 - s3) | (s2 - s1 - s3) | (s3 - s1 - s2) # "|" unión de conjuntos (suma) y "-" es la diferencia de conjuntos (resta)
    return list(unique_gifts)
    """


def test(e, r):
    return e == r


def main():
    a1 = ['bici', 'coche', 'bici', 'bici']
    a2 = ['coche', 'bici', 'muñeca', 'coche']
    a3 = ['bici', 'pc', 'pc']

    """
    El almacén a1 tiene "bici" y "coche".
    El almacén a2 tiene "coche", "bici" y "muñeca".
    El almacén a3 tiene "bici" y "pc".

    El regalo "muñeca" y "pc" sólo están en los almacenes a2 y a3 respectivamente.
    """

    gifts = getGiftsToRefill(a1, a2, a3) # ['muñeca', 'pc']

    print(test(["muñeca", "pc"], gifts))


if __name__ == "__main__":
    main()