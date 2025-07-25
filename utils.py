def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diags
    ]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != ' ':
            return board[i]
    if is_full(board):
        return 'Tie'
    return None

def is_full(board):
    return all(cell != ' ' for cell in board)

def minimax(board, current, ai, human):
    winner = check_winner(board)
    if winner == ai:
        return (1, None)
    elif winner == human:
        return (-1, None)
    elif is_full(board):
        return (0, None)

    best_score = -float('inf') if current == ai else float('inf')
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = current
            score, _ = minimax(board, human if current == ai else ai, ai, human)
            board[i] = ' '

            if current == ai:
                if score > best_score:
                    best_score = score
                    best_move = i
            else:
                if score < best_score:
                    best_score = score
                    best_move = i

    return best_score, best_move
