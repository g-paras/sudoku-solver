#easy  43 spaces
b1 = [
	[0, 0, 0, 0, 7, 8, 0, 0, 5],
	[0, 0, 5, 4, 2, 9, 0, 0, 0],
	[7, 3, 0, 0, 0, 1, 0, 9, 0],
	[0, 7, 0, 0, 0, 0, 0, 2, 0],
	[9, 0, 6, 0, 0, 0, 5, 0, 7],
	[1, 2, 0, 0, 0, 5, 9, 3, 6],
	[0, 6, 9, 0, 5, 7, 0, 8, 1],
	[3, 0, 1, 9, 0, 0, 0, 6, 0],
	[2, 0, 0, 6, 1, 0, 4, 5, 0]
]

#hard  58 spaces 
b2 = [
	[1, 3, 0, 0, 0, 5, 0, 4, 0],
	[0, 0, 0, 7, 3, 0, 0, 0, 0],
	[7, 0, 0, 0, 1, 9, 0, 0, 0],
	[0, 0, 6, 0, 0, 0, 1, 0, 9],
	[0, 0, 9, 8, 0, 0, 0, 0, 2],
	[8, 7, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 8, 0, 0, 0],
	[0, 0, 0, 3, 4, 0, 0, 6, 0],
	[6, 0, 0, 0, 0, 0, 0, 0, 5]
]

#almost impossible  79 spaces
b3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 2, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-------------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(str(board[i][j]))
            elif j == 0:
                print("  " + str(board[i][j]) + " ", end="")
            else:
                print(str(board[i][j]) + " ", end="")


def valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num:
            return False

    for i in range(9):
        if board[i][pos[1]] == num:
            return False

    a = pos[0]//3
    b = pos[1]//3

    for i in range(a*3, a*3 + 3):
        for j in range(b*3, b*3 + 3):
            if board[i][j] == num:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return False


def solve(board):
    find = find_empty(board)

    if not find_empty(board):
        return True

    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def count_zeros(board):
    count = 0
    for i in board:
        for j in i:
            if j == 0:
                count += 1

    print(count)


if __name__ == '__main__':
    board = b3
    print("\n" + "Unsolved Board".center(25, "~") + "\n")
    print_board(board)
    print("\n" + "Solved Board".center(25, "~") + "\n")
    solve(board)
    print_board(board)
    # count_zeros(board)
