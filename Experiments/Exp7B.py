def board(row, col):
    for i in range(row):
        print("  --- " * col)
        print("|     " * (col + 1))
    print("  --- " * col)


row = int(input("Enter row size of board:"))
col = int(input("Enter col size of board:"))
board(row, col)
