"""En la fábrica de juguetes del Polo Norte, cada juguete tiene un número de identificación único.

Sin embargo, debido a un error en la máquina de juguetes, algunos números se han asignado a más de un juguete.

¡Encuentra el primer número de identificación que se ha repetido, donde la segunda ocurrencia tenga el índice más pequeño!

En otras palabras, si hay más de un número repetido, debes devolver el número cuya segunda ocurrencia aparezca primero en la lista. Si no hay números repetidos, devuelve -1.

¡Ojo! Los elfos dicen que esto es una prueba técnica de Google."""


def findFirstRepeated(gifts: list[int]) -> int:
    unique_gifts = set()

    for gift in gifts:
        if gift in unique_gifts: return gift
        unique_gifts.add(gift)
    
    return -1

def test(e, r) -> bool:
    return e == r


def main():
    giftIds = [2, 1, 3, 5, 3, 2]
    firstRepeatedId = findFirstRepeated(giftIds)
    print(test(3, firstRepeatedId)) # 3
    # Aunque el 2 y el 3 se repiten
    # el 3 aparece primero por segunda vez

    giftIds2 = [1, 2, 3, 4]
    firstRepeatedId2 = findFirstRepeated(giftIds2)
    print(test(-1, firstRepeatedId2)) # -1
    # Es -1 ya que no se repite ningún número

    giftIds3 = [5, 1, 5, 1]
    firstRepeatedId3 = findFirstRepeated(giftIds3)
    print(test(5, firstRepeatedId3)) # 5


if __name__ == "__main__":
    main()