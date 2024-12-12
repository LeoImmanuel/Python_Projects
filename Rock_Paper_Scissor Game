import random

def play() -> str:
    while True:
        # User and Computer choice for the play
        user_choice = input("What's your choice? Rock 'r', Paper 'p', Scissors 's': ").lower()

        # Validate user choice
        if user_choice not in ["r", "p", "s"]:
            print("Invalid choice! Please choose 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(["r", "p", "s"])

        # Tie condition
        if user_choice == computer_choice:
            print(f"It's a tie!\nUser choice: {user_choice}\nOpponent choice: {computer_choice}")
        # Function to evaluate who wins, pass the user and computer choice
        elif is_win(user_choice, computer_choice):
            # Winning condition for the user
            print(f"You won!\nUser choice: {user_choice}\nOpponent choice: {computer_choice}")
        else:
            # Losing condition
            print(f"You lost!\nUser choice: {user_choice}\nOpponent choice: {computer_choice}")

        # Replay prompt
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

def is_win(player: str, opponent: str) -> bool:
    # Winning conditions for the player
    return (
        (player == 'r' and opponent == 's') or
        (player == 's' and opponent == 'p') or
        (player == 'p' and opponent == 'r')
    )

# Start the game
play()
