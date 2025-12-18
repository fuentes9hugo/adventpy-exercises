"""La fábrica de Santa ha empezado a recibir la lista de producción de juguetes.
Cada línea indica qué juguete hay que fabricar y cuántas unidades.

Los elfos, como siempre, han metido la pata: han apuntado algunos juguetes con cantidades que no tienen sentido.

Tienes una lista de objetos con esta forma:

toy: el nombre del juguete (string)
quantity: cuántas unidades hay que fabricar (number)
Tu tarea es escribir una función que reciba esta lista y devuelva un array de strings con:

Cada juguete repetido tantas veces como indique quantity
En el mismo orden en el que aparecen en la lista original
Ignorando los juguetes con cantidades no válidas (menores o iguales a 0, o que no sean número)"""


# Ineficiente, con list compreheison creas una lista que no usas y haces muchos append consecutivos que con extend puedes agrupar
"""def manufactureGifts(gifts_to_produce: list[dict[str, int]]) -> list[str]:
    gifts = []
    for gift in gifts_to_produce:
        if gift["quantity"] > 0:
            [gifts.append(gift["toy"]) for _ in range(gift["quantity"])]
            
    return gifts"""


def manufactureGifts(gifts_to_produce):
    gifts = []
    for gift in gifts_to_produce:
        if gift["quantity"] > 0:
            gift_times = [gift["toy"]] * gift["quantity"]
            gifts.extend(gift_times)
            
    return gifts


def main():
    production1 = [
        { "toy": 'car', "quantity": 3 },
        { "toy": 'doll', "quantity": 1 },
        { "toy": 'ball', "quantity": 2 }
    ]
    print(manufactureGifts(production1))
    # ['car', 'car', 'car', 'doll', 'ball', 'ball']

    production2 = [
        { "toy": 'train', "quantity": 0 }, # no se fabrica
        { "toy": 'bear', "quantity": -2 }, # tampoco
        { "toy": 'puzzle', "quantity": 1 }
    ]
    print(manufactureGifts(production2))
    # ['puzzle']

    production3 = []
    print(manufactureGifts(production3))
    # []

if __name__ =="__main__":
    main()