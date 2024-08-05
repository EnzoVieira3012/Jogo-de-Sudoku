import random


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else '.', end=" ")
        print()


def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def generate_board():
    base = 3
    side = base * base

    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    def shuffle(s): return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties): board[p // side][p % side] = 0
    return board


def main():
    print("Bem-vindo ao Sudoku!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Gerar novo quebra-cabeça de Sudoku")
        print("2. Fornecer quebra-cabeça de Sudoku")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            board = generate_board()
            print("\nQuebra-cabeça gerado:")
            print_board(board)

            if solve_sudoku([row[:] for row in board]):
                print("\nResolução do quebra-cabeça:")
                print_board(board)
            else:
                print("Não foi possível resolver o quebra-cabeça.")

        elif choice == '2':
            board = []
            print("\nDigite o quebra-cabeça linha por linha (use 0 para células vazias, separadas por espaços):")
            for _ in range(9):
                row = list(map(int, input().split()))
                if len(row) != 9:
                    print("Cada linha deve conter 9 números.")
                    return
                board.append(row)

            print("\nQuebra-cabeça fornecido:")
            print_board(board)

            if solve_sudoku(board):
                print("\nResolução do quebra-cabeça:")
                print_board(board)
            else:
                print("Não foi possível resolver o quebra-cabeça.")

        elif choice == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
