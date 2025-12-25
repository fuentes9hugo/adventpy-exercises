def n_queens(num_of_queens: int):
    board = [[" " for row in range(num_of_queens)] for col in range(num_of_queens)]

    def backtrack(actual_queens: list[tuple[int, int]], row_index: int, cols: set, diagonals: set, antidiagonals: set) -> list[tuple[int, int]]:
        if row_index == num_of_queens: return actual_queens
        
        for j in range(len(board[row_index])):
            if j in cols: continue

            if row_index + j in diagonals or row_index - j in antidiagonals: continue

            queen = (row_index, j)
            
            actual_queens.append(queen)
            cols.add(j)
            diagonals.add(row_index + j)
            antidiagonals.add(row_index - j)

            current_queens = backtrack(actual_queens, row_index + 1, cols, diagonals, antidiagonals)

            if len(current_queens) == num_of_queens:
                    return current_queens
            
            actual_queens.remove(queen)
            cols.remove(j)
            diagonals.discard(row_index + j)
            antidiagonals.remove(row_index - j)
        
        return actual_queens
                
    queens = backtrack([], 0, set(), set(), set())

    for queen_y, queen_x in queens: board[queen_y][queen_x] = "Q"

    for row in board: print(row)

    return queens


def main():
    print(n_queens(8))
    print("\n\n")
    print(n_queens(4))
    print("\n\n")
    print(n_queens(2))
    print("\n\n")
    print(n_queens(16))


if __name__ == "__main__":
    main()