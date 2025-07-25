from utils import print_board, check_winner, minimax, is_full

def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                return move
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 1 to 9.")

def main():
    board = [' '] * 9
    human = 'O'
    ai = 'X'
    current_player = human  # human starts

    print("Welcome to AI Tic-Tac-Toe!")
    print_board(board)

    while True:
        if current_player == human:
            move = get_human_move(board)
            board[move] = human
        else:
            print("AI is thinking...")
            _, move = minimax(board, ai, ai, human)
            board[move] = ai

        print_board(board)

        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        current_player = ai if current_player == human else human

if __name__ == "__main__":
    main()
