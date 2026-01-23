from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    board.insert_piece()
    print(board.draw())
    board.move_piece_down()
    print(board.draw())
    board.rotate_current_piece("w")
    board.move_piece_down()
    print(board.draw())
    board.move_piece_horizontally("d")
    print(board.draw())
    board.move_piece_horizontally("d")
    print(board.draw())
    board.rotate_current_piece("w")
    board.move_piece_horizontally("d")
    print(board.draw())
    board.move_piece_horizontally("d")
    board.rotate_current_piece("s")
    print(board.draw())
    board.move_piece_horizontally("d")
    print(board.draw())
    board.move_piece_horizontally("a")
    print(board.draw())


if __name__ == "__main__":
    main()