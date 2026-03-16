"""El día se acerca y Papá Noel tiene el almacén de juguetes hecho un desastre. Ayúdale a ordenar los juguetes en el almacén para que pueda encontrarlos más fácilmente.

Para ello, nos dan dos arrays. El primero es un array de juguetes, y el segundo es un array de números que indican la posición de cada juguete en el almacén.

Lo único a tener en cuenta es que las posiciones pueden no empezar en 0, aunque siempre serán números consecutivos y de forma ascendente.

Tenemos que devolver un array donde cada juguete esté en la posición que le corresponde.

A tener en cuenta
- Siempre habrá el mismo número de juguetes que de posiciones.
- Ni los juguetes ni las posiciones se repiten."""


def sortToys(toys: list[str], positions: list[int]) -> list[str]:
    # return  [gift[0] for gift in sorted(zip(toys, positions), key=lambda x: x[1])] -- oneline solution
    
    ordered_gifts = sorted(zip(toys, positions), key=lambda x: x[1])
    ordered_gifts = [gift[0] for gift in ordered_gifts]
    
    return ordered_gifts


def test(e, r):
    return e == r


def main():
    toys = ['ball', 'doll', 'car', 'puzzle']
    positions = [2, 3, 1, 0]

    print(test(['puzzle', 'car', 'ball', 'doll'], sortToys(toys, positions)))
    # ['puzzle', 'car', 'ball', 'doll']

    moreToys = ['pc', 'xbox', 'ps4', 'switch', 'nintendo']
    morePositions = [8, 6, 5, 7, 9]

    print(test(['ps4', 'xbox', 'switch', 'pc', 'nintendo'], sortToys(moreToys, morePositions)))
    # ['ps4', 'xbox', 'switch', 'pc', 'nintendo']


if __name__ == "__main__":
    main()