def board(row, col):
    for i in range(row):
        print("  --- " * col)
        print("|     " * (col + 1))
    print("  --- " * col)


row = input("Enter row size of board:")
col = input("Enter col size of board:")
board(int(row), int(col))

