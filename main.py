from board import createboard, print_board, AI, HUMAN
from player_input import human_move
from ai import minimax
from rules import game_over, evaluate

def play_game():
    board = createboard()
    turn = HUMAN  # Human starts

    while not game_over(board):
        print_board(board)
        if turn == HUMAN:
            print("Your move:")
            human_move(board)
            turn = AI
        else:
            print("AI is thinking...")
            _, board = minimax(board, 3, True)
            turn = HUMAN

    print_board(board)
    score = evaluate(board)
    if score > 0:
        print("AI (R) wins!")
    elif score < 0:
        print("You (B) win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()