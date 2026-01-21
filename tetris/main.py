from models import Board, Piece, O, I, T, S, Z, L, J


def main():
    board = Board()
    t = O()
    board.current_piece = t
    board.insert_piece()
    for i in board.grid:
        print("".join(i))


if __name__ == "__main__":
    main()