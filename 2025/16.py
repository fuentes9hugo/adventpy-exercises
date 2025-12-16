"""Santa quiere repartir regalos de la forma más eficiente posible 🎁. Tiene una lista de regalos, cada uno con un peso, y un trineo que solo puede cargar hasta un peso máximo.

Los regalos se entregan en orden, y Santa no puede cambiar ese orden. Cuando un regalo no cabe en el trineo actual, Santa envía el trineo y prepara uno nuevo.

Tu tarea es escribir una función que calcule el número mínimo de trineos necesarios para entregar todos los regalos.

Eso sí, ten en cuenta que a veces hay un regalo que no cabe en el trineo, entonces hay que devolver null porque ese trineo no sirve para ese pack de regalos."""


def packGifts(gifts: list[int], maxWeight: int) -> int | None:
    if not gifts: return 0
    
    num_of_sleds = 1
    current_sled_weight = 0

    for gift in gifts:
        if gift > maxWeight: return None

        if current_sled_weight + gift > maxWeight:
            num_of_sleds += 1
            current_sled_weight = gift
            continue
        
        current_sled_weight += gift
    
    return num_of_sleds


def test(expected, received):
    return expected == received


def main():
    print(test(2, packGifts([2, 3, 4, 1], 5)))
    # 2 trineos
    # Trineo 1: 2 + 3 = 5
    # Trineo 2: 4 + 1 = 5

    print(test(3, packGifts([3, 3, 2, 1], 3)))
    # 3 trineos
    # Trineo 1: 3
    # Trineo 2: 3
    # Trineo 3: 2 + 1 = 3

    print(test(2, packGifts([1, 1, 1, 1], 2)))
    # 2 trineos
    # Trineo 1: 1 + 1 = 2
    # Trineo 2: 1 + 1 = 2

    print(test(None, packGifts([5, 6, 1], 5)))
    # null
    # Hay un regalo de peso 6 que no cabe

    print(test(0, packGifts([], 10)))
    # 0 trineos
    # No hay regalos que entregar


if __name__ == "__main__":
    main()