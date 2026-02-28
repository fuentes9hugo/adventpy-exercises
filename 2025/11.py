"""El grinch quiere robar los regalos de Navidad del almacén. Para ello necesita saber qué regalos no tienen vigilancia.

El almacén se representa como un array de strings (string[]), donde cada regalo (*) está protegido si su posición está junto a una cámara (#). Cada espacio vacío se representa con un punto (.).

Tu tarea es contar cuántos regalos están sin vigilancia, es decir, que no tienen ninguna cámara adyacente (arriba, abajo, izquierda o derecha).

Ten en cuenta: solo se considera como "adyacente" las 4 direcciones cardinales, no en diagonal.

Los regalos en las esquinas o bordes pueden estar sin vigilancia, siempre que no tengan cámaras directamente al lado."""


def findUnsafeGifts(warehouse: list[str]) -> int:
    gifts = []
    cameras = []

    for i, row in enumerate(warehouse):
        if "*" in row or "#" in row:
            for j, char in enumerate(row):
                if char == "*":
                    gifts.append((i, j))
                
                elif char == "#":
                    cameras.append((i, j))
    
    unsafed_gifts = 0

    for gift in gifts:
        if any(gift[0] == camera[0] and gift[1] - camera[1] in (1, -1) or gift[1] == camera[1] and gift[0] - camera[0] in (1, -1) for camera in cameras):
            continue
        
        unsafed_gifts += 1
    
    return unsafed_gifts


def test(expected, received):
    return expected == received


def main():
    print(test(0, findUnsafeGifts([
        '.*.',
        '*#*',
        '.*.'
    ]))) # ➞ 0

    # Todos los regalos están junto a una cámara

    print(test(1, findUnsafeGifts([
        '...',
        '.*.',
        '...'
    ]))) # ➞ 1

    # Este regalo no tiene cámaras alrededor

    print(test(2, findUnsafeGifts([
        '*.*',
        '...',
        '*#*'
    ]))) # ➞ 2
    # Los regalos en las esquinas superiores no tienen cámaras alrededor

    print(test(4, findUnsafeGifts([
        '.....',
        '.*.*.',
        '..#..',
        '.*.*.',
        '.....'
    ]))) # ➞ 4

    # Los cuatro regalos no tienen cámaras, porque están en diagonal a la cámara

    print(test(0, findUnsafeGifts([
        '#*.',
        '...',
        '..#'
    ]))) # ➞ 0

    print(test(0, findUnsafeGifts([
        '...#....',
        '..*#*..',
        '...#....'
    ]))) # ➞ 0

    print(test(4, findUnsafeGifts([
        '*.*',
        '...',
        '*.*'
    ]))) # ➞ 4


if __name__ == "__main__":
    main()