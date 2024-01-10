def Board(board):
    print("   0 1 2")
    for i, row in enumerate(board):
        print(f"{i} |" + "|".join(row) + "|")
        if i < 2:
            print("  -------")


def check_victory(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for _ in range(9):
        Board(board)
        print(f"Ход игрока {player}")

        try:
            line = int(input("Введите номер строки (0, 1, 2): "))
            column = int(input("Введите номер столбца (0, 1, 2): "))

            if 0 <= line <= 2 and 0 <= column <= 2 and board[line][column] == " ":
                board[line][column] = player

                if check_victory(board, player):
                    Board(board)
                    print(f"Игрок {player} победил!")
                    break

                player = "O" if player == "X" else "X"
            else:
                print("Недопустимый ход. Введите корректные значения.")
        except ValueError:
            print("Некорректный ввод. Введите числа от 0 до 2.")

    print("Игра завершена.")

if __name__ == "__main__":
    main()