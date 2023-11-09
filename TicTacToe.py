# Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# Function to check if the game is over
def game_over(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

# Function to evaluate the board for Minimax
def evaluate_board(board):
    for row in board:
        if row.count('X') == 3:
            return 10
        if row.count('O') == 3:
            return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta):
    if game_over(board):
        return evaluate_board(board)
    
    if is_full(board):
        return 0

    if is_max:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_eval = -float("inf")
    best_move = (-1, -1)
    alpha = -float("inf")
    beta = float("inf")
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main game loop
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_full(board) and not game_over(board):
        # Player's turn
        row, col = map(int, input("Enter your move (row and column, e.g., 1 2): ").split())
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row - 1][col - 1] = 'O'
        print_board(board)

        if game_over(board):
            print("Congratulations! You won!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI's turn:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'X'
        print_board(board)

        if game_over(board):
            print("AI wins! Better luck next time.")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
