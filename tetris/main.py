from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    board.insert_piece()
    print(board.draw())
    board.move_piece_down()
    print(board.draw())


if __name__ == "__main__":
    main()