from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    board.insert_piece()
    for row in board.grid:
        print("".join(row))


if __name__ == "__main__":
    main()