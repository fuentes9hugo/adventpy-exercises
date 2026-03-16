"""Estamos preparando los sacos para los regalos de Navidad pero cada saco tiene un límite de peso.

Nos dan un array con los nombres de los regalos y un número que es el peso máximo que puede llevar cada saco. El peso de cada regalo es la longitud de su nombre.

Escribe una función que agrupe los regalos en sacos y devuelva un array con los nombres de los regalos de cada saco. Para agrupar los regalos, se separan los nombres por espacios (el espacio no cuenta como peso).

¡Pero ojo! Cada saco puede llevar un máximo de peso, y si el peso de los regalos de un saco supera el peso máximo, se debe separar el último regalo del saco y ponerlo en el siguiente saco.

Ten en cuenta:
- Los regalos siempre se agrupan por orden de aparición en el array.
- No puedes cambiar el orden de los regalos en el array a la hora de agruparlos.
- Se pueden agrupar todos los regalos en un solo saco.
- Si no se puede agrupar ningún regalo en un saco, se devuelve un array vacío."""

def carryGifts(gifts: list[str], maxWeight: int) -> list[str]:
    grouped_sacks = []
    sack = []
    actual_weight = 0

    for gift in gifts:
        gift_weight = len(gift)
        if gift_weight > maxWeight: continue

        if actual_weight + gift_weight > maxWeight:
            grouped_sacks.append(" ".join(sack))
            sack = []
            actual_weight = 0

        sack.append(gift)
        actual_weight += gift_weight
    
    if sack: grouped_sacks.append(" ".join(sack))

    return grouped_sacks


def test(e, r):
    return e == r


def main():
    print(test(['game bike', 'book toy'], carryGifts(['game', 'bike', 'book', 'toy'], 10)))
    print(test(['game', 'bike', 'book toy'], carryGifts(['game', 'bike', 'book', 'toy'], 7)))
    print(test(['game', 'bike', 'book', 'toy'], carryGifts(['game', 'bike', 'book', 'toy'], 4)))
    print(test(['toy', 'gamme', 'toy', 'bike'],carryGifts(['toy', 'gamme', 'toy', 'bike'], 6)))
    print(test([], carryGifts(['toyerfefhh', 'gammewefwefwef', 'toywedwedwed', 'bikeewdwed'], 6)))
    print(test(["t g t b"], carryGifts(['t', 'g', 't', 'b'], 6)))


if __name__ == "__main__":
    main()