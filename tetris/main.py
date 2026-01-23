from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    print(board)
    board.insert_piece()
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_down()
    print(board.draw())
    print(board.current_piece.grid_position)
    board.rotate_current_piece("w")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.move_piece_horizontally("a")
    print(board.draw())
    print(board.current_piece.grid_position)
    board.rotate_current_piece("s")
    print(board.draw())
    print(board.current_piece.grid_position)
    """
    board.move_piece_horizontally("d")
    board.move_piece_horizontally("d")
    board.move_piece_horizontally("d")
    print(board.draw())"""



if __name__ == "__main__":
    main()