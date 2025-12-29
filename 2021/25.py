"""Ayer, en noche buena, una família cenó por todo lo alto... Con tanta copa 🍾 encima todavía no han retirado los platos y la comida de ayer...

Un ratoncillo llamado midurat 🐭, que vió ayer el festín escondido, está relamiéndose los bigotes al ver todos los manjares que hay en el comedor.

Eso sí, hay que tener cuidado 😶 y sólo hacer los movimientos correctos para comer algo. Por eso, el ratón, que se ha visto los vídeos de midudev, va a crear una función para saber si su próximo movimiento es correcto o no ✅.

El ratoncillo se puede mover en 4 direcciones: up, down, left, right y el comedor es una matriz (un array de arrays) donde cada posición puede ser:

Un espacio vacío es que no hay nada
Una m es el ratón
Un * es la comida
Vamos a ver unos ejemplos.

¡Ten en cuenta que el ratón quiere buscar comida en diferentes habitaciones y que cada una puede tener dimensiones diferentes!"""


def canMouseEat(direction: str, game: list[list[str]]) -> bool:
    pass


def test(expected, received):
    return expected == received


def main():
    room = [
    [' ', ' ', ' '],
    [' ', ' ', 'm'],
    [' ', ' ', '*']
    ]

    print(test(False, canMouseEat('up',    room)))   # false
    print(test(True, canMouseEat('down',  room)))   # true
    print(test(False, canMouseEat('right', room)))   # false
    print(test(False, canMouseEat('left',  room)))   # false

    room2 = [
    ['*', ' ', ' ', ' '],
    [' ', 'm', '*', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', '*']
    ]

    print(test(False, canMouseEat('up',    room2)))   # false
    print(test(False, canMouseEat('down',  room2)))   # false
    print(test(True, canMouseEat('right', room2)))   # true
    print(test(False, canMouseEat('left',  room2)))   # false


if __name__ == "__main__":
    main()