# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row.count(player) == 3:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full (draw)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to take player input and update the board
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("That spot is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number between 1 and 3.")

# Main function to control the game flow
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board initialized with empty spaces
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        # Check for win or draw
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
