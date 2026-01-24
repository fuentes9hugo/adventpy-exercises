from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    print(board)
    board.remover()
    print(board)


if __name__ == "__main__":
    main()