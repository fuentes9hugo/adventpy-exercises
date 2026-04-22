"""En el taller de Santa, los elfos tienen una lista de regalos que desean fabricar y un conjunto limitado de materiales.

Los regalos son cadenas de texto y los materiales son caracteres. Tu tarea es escribir una función que, dada una lista de regalos y los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.

Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo."""


def manufacture(gifts: list[str], materials: str) -> list[str]:
    materials_set = set(materials)

    available_gifts = []

    for gift in gifts:
        if all(char in materials_set for char in gift): available_gifts.append(gift)
    
    return available_gifts

"""
def manufacture(gifts: list[str], materials: str) -> list[str]:
    materials_set = set(materials)
    return [gift for gift in gifts if set(gift).issubset(materials_set)]
"""


def test(e, r):
    return e == r


def main():
    gifts = ['tren', 'oso', 'pelota']
    materials = 'tronesa'

    print(test(["tren", "oso"], manufacture(gifts, materials))) # ["tren", "oso"]
    # 'tren' SÍ porque sus letras están en 'tronesa'
    # 'oso' SÍ porque sus letras están en 'tronesa'
    # 'pelota' NO porque sus letras NO están en 'tronesa'

    gifts = ['juego', 'puzzle']
    materials = 'jlepuz'

    print(test(["puzzle"], manufacture(gifts, materials))) # ["puzzle"]

    gifts = ['libro', 'ps5']
    materials = 'psli'

    print(test([], manufacture(gifts, materials))) # []


if __name__ == "__main__":
    main()