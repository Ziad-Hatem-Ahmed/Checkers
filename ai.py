from rules import get_all_moves, evaluate, game_over
from board import AI, HUMAN

def minimax(board, depth, maximizing):
    if depth == 0 or game_over(board):
        return evaluate(board), board

    if maximizing:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(board, AI):
            eval, _ = minimax(move, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(board, HUMAN):
            eval, _ = minimax(move, depth - 1, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move