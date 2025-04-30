from board import BOARD_SIZE, EMPTY, HUMAN, AI

def human_move(board):
    while True:
        try:
            row = int(input("Enter the row of the piece you want to move: "))
            col = int(input("Enter the column of the piece you want to move: "))
            direction = input("Enter direction (left or right): ").strip().lower()

            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                print("Invalid position.")
                continue

            if board[row][col] != HUMAN:
                print("No human piece at that position.")
                continue

            dir_offset = -1 if direction == "left" else 1 if direction == "right" else None
            if dir_offset is None:
                print("Invalid direction.")
                continue

            new_row = row + 1
            new_col = col + dir_offset

            # Jump move
            if (0 <= row + 2 < BOARD_SIZE and 0 <= col + 2 * dir_offset < BOARD_SIZE):
                enemy = board[row + 1][col + dir_offset]
                target = board[row + 2][col + 2 * dir_offset]
                if enemy == AI and target == EMPTY:
                    board[row][col] = EMPTY
                    board[row + 1][col + dir_offset] = EMPTY
                    board[row + 2][col + 2 * dir_offset] = HUMAN
                    break

            # Normal move
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE and board[new_row][new_col] == EMPTY:
                board[row][col] = EMPTY
                board[new_row][new_col] = HUMAN
                break
            else:
                print("Invalid move.")
        except Exception as e:
            print("Error:", e)