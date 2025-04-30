import copy
from board import EMPTY, AI, HUMAN, BOARD_SIZE

def evaluate(board):
    red = sum(row.count(AI) for row in board)
    black = sum(row.count(HUMAN) for row in board)
    return red - black

def get_all_moves(board, player):
    moves = []
    direction = -1 if player == AI else 1

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == player:
                for dx in [-1, 1]:
                    ni, nj = i + direction, j + dx
                    if 0 <= ni < BOARD_SIZE and 0 <= nj < BOARD_SIZE and board[ni][nj] == EMPTY:
                        new_board = copy.deepcopy(board)
                        new_board[i][j] = EMPTY
                        new_board[ni][nj] = player
                        moves.append(new_board)

                    # Jump
                    ni2, nj2 = i + 2 * direction, j + 2 * dx
                    mi, mj = i + direction, j + dx
                    if (0 <= ni2 < BOARD_SIZE and 0 <= nj2 < BOARD_SIZE and
                        0 <= mi < BOARD_SIZE and 0 <= mj < BOARD_SIZE and
                        board[mi][mj] != EMPTY and board[mi][mj] != player and board[ni2][nj2] == EMPTY):
                        new_board = copy.deepcopy(board)
                        new_board[i][j] = EMPTY
                        new_board[mi][mj] = EMPTY
                        new_board[ni2][nj2] = player
                        moves.append(new_board)
    return moves

def game_over(board):
    return not get_all_moves(board, AI) or not get_all_moves(board, HUMAN)