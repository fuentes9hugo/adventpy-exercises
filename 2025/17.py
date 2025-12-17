"""En el Polo Norte han montado un panel de luces navideñas 🎄✨ para decorar el taller. Cada luz puede estar encendida con un color o apagada.

El panel se representa como una matriz donde cada celda puede ser:

'.' → luz apagada
'R' → luz roja
'G' → luz verde
Los elfos quieren saber si en el panel existe una línea de 4 luces del mismo color encendidas y alineadas (solo horizontal ↔ o vertical ↕). Las luces apagadas ('.') no cuentan.

Nota: El tablero puede ser de cualquier tamaño. No hay diagonales."""


def hasFourLights(board: list[list[str]]) -> bool:
    targets = ("RRRR", "GGGG")

    for row in board:
        row_str = "".join(row)
        if any(target in row_str for target in targets):
            return True
    
    # --- IMPORTANTE ---
    # Para transponer una lista de listas -> zip(*lista_de_listas)
    # * -> se encarga de desempaquetar la lista de listas en listas independientes (Si board es [fila1, fila2], pasa a ser: zip(fila1, fila2))
    # zip -> agrupa los elementos del mismo índice. Toma el índice 0 de todas las filas, luego el 1, etc. (i = 0 -> lista1[i], lista2[i]...)
    # col -> es la variable que recoge todos los valores. Al usar únicamente una variable, se empaquetan todos los valores en una tupla
    for col in zip(*board):
        col_str = "".join(col)
        if any(target in col_str for target in targets):
            return True

    return False


def test(expected, received):
    return expected == received


def main():
    print(test(True, hasFourLights([
        ['.', '.', '.', '.', '.'],
        ['R', 'R', 'R', 'R', '.'],
        ['G', 'G', '.', '.', '.']
    ])))
    # true → hay 4 luces rojas en horizontal

    print(test(True, hasFourLights([
        ['.', 'G', '.', '.'],
        ['.', 'G', '.', '.'],
        ['.', 'G', '.', '.'],
        ['.', 'G', '.', '.']
    ])))
    # true → hay 4 luces verdes en vertical

    print(test(False, hasFourLights([
        ['R', 'G', 'R'],
        ['G', 'R', 'G'],
        ['G', 'R', 'G']
    ])))
    # false → no hay 4 luces del mismo color seguidas


if __name__ == "__main__":
    main()