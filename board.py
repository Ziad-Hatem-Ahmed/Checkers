EMPTY = '.'
AI = 'R'
HUMAN = 'B'
BOARD_SIZE = 8

def createboard():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for i in range(3):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = HUMAN
    for i in range(5, 8):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = AI
    return board

def print_board(board):
    print("  " + " ".join(str(j) for j in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()