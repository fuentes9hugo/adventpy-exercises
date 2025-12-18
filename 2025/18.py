"""El panel de luces navideñas 🎄✨ del taller ha sido un éxito total. Pero los elfos quieren ir un paso más allá: ahora quieren detectar si hay una línea de 4 luces del mismo color también en diagonal.

El panel sigue siendo una matriz donde cada celda puede ser:

'.' → luz apagada
'R' → luz roja
'G' → luz verde
Ahora tu función debe devolver true si existe una línea de 4 luces del mismo color encendidas y alineadas, ya sea horizontal ↔, vertical ↕ o diagonal ↘↙.

Nota: El tablero puede ser de cualquier tamaño."""


def hasFourInARow(board: list[list[str]]) -> bool:
    board_len = len(board)
    board_len_over_4 = board_len - 4

    targets = ("RRRR", "GGGG")

    def check_row(board):
        for row in board:
            row_str = "".join(row)
            if any(target in row_str for target in targets):
                return True
        
        return False


    def check_col(board):
        for col in zip(*board):
            col_str = "".join(col)
            if any(target in col_str for target in targets):
                return True
        
        return False


    def check_diagonal(board):
        for i in range(board_len_over_4 + 1):
            diagonal = []
            diagonal_2 = []
            for j in range(board_len - i):
                diagonal.append(board[j + i][j])
                diagonal_2.append(board[j][j + i])
            
            diagonal = "".join(diagonal)
            diagonal_2 = "".join(diagonal_2)
            if any(t in diagonal or t in diagonal_2 for t in targets):
                return True
        
        return False

    return True if check_row(board) or check_col(board) or check_diagonal(board) or check_diagonal(board[::-1]) else False


def test(expected, received):
    return expected == received


def main():
    print(test(True, hasFourInARow([
    ['R', '.', '.', '.'],
    ['.', 'R', '.', '.'],
    ['.', '.', 'R', '.'],
    ['.', '.', '.', 'R']
    ])))
    # true → hay 4 luces rojas en diagonal ↘

    print(test(True, hasFourInARow([
    ['.', '.', '.', 'G'],
    ['.', '.', 'G', '.'],
    ['.', 'G', '.', '.'],
    ['G', '.', '.', '.']
    ])))
    # true → hay 4 luces verdes en diagonal ↙

    print(test(True, hasFourInARow([
    ['R', 'R', 'R', 'R'],
    ['G', 'G', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.']
    ])))
    # true → hay 4 luces rojas en horizontal

    print(test(False, hasFourInARow([
    ['R', 'G', 'R'],
    ['G', 'R', 'G'],
    ['G', 'R', 'G']
    ])))
    # false → no hay 4 luces del mismo color seguidas

    print(test(True, hasFourInARow([
    ['R', 'R', '.', '.', '.', '.'],
    ['R', '.', 'R', '.', '.', '.'],
    ['.', 'R', '.', 'R', '.', '.'],
    ['.', '.', '.', '.', "R", '.'],
    ['.', '.', '.', '.', '.', "R"],
    ['.', '.', '.', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'R', '.', '.'],
    ['.', '.', 'R', '.', ".", '.'],
    ['.', 'R', '.', '.', '.', "."],
    ['R', '.', '.', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'G'],
    ['.', '.', '.', '.', "G", '.'],
    ['.', '.', '.', 'G', '.', "."],
    ['.', '.', 'G', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', 'G', '.', '.', '.'],
    ['.', '.', 'R', 'G', '.', '.', '.'],
    ['.', 'G', 'G', '.', '.', '.', '.'],
    ['R', 'G', '.', '.', ".", '.', '.'],
    ['G', '.', '.', '.', '.', ".", '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'G', '.'],
    ['.', '.', 'G', '.', '.'],
    ['.', 'G', '.', '.', "."],
    ['G', '.', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', '.', 'G'],
    ['.', '.', '.', 'G', '.'],
    ['.', '.', 'G', '.', '.'],
    ['.', 'G', '.', '.', "."],
    ['.', '.', '.', '.', '.']
    ])))
    # true

    print(test(False, hasFourInARow([
    ['.', '.', '.', '.', 'R'],
    ['.', '.', '.', 'R', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', 'R', '.', "."],
    ['.', 'R', '.', '.', '.']
    ])))
    # false

    print(test(True, hasFourInARow([
    ['.', '.', '.', 'R', '.'],
    ['.', '.', 'R', '.', '.'],
    ['.', 'R', '.', '.', '.'],
    ['R', '.', '.', '.', "."],
    ['.', '.', '.', '.', '.']
    ])))
    # true

    print(test(True, hasFourInARow([
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'G'],
    ['.', '.', '.', 'G', '.'],
    ['.', '.', 'G', '.', "."],
    ['.', 'G', '.', '.', '.']
    ])))
    # true


if __name__ == "__main__":
    main()