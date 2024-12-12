import random

def user_guess(x:int)->str:
    # Number that needs to be guessed stored in variable "random_number" 
    random_number = random.randint(1,x)
    # Initialzing user input to default "False"
    user_guess = 0
    # Take input from user until user_guess is "True"
    while user_guess != random_number:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        # If user guess was low, display message "too low"
        if user_guess < random_number:
            print(f"Try again..{user_guess} is too low")
        # If user guess was high, display message "too high"
        elif user_guess > random_number:
            print(f"Try again..{user_guess} is too high")
    # Message when user guessed it correct
    print(f"Yay, Awesome. You have guessed  the number {random_number} correctly")

def computer_guess(x):
    print(f"Guess a number between 1 to {x}")
    # start & end pointers for range of numbers to guess from
    start = 1
    end = x
    # Default User input is NULL or Empty string
    user_feedback = ''
    # Runs until User input is 'c' Note: c means computer has guessed number correctly
    while user_feedback != 'c':
        # Until start & ends pointers are not equal or doesn't point to same number, recieve input from computer 
        if start != end:
            comp_guess = random.randint(start,end)
        # Once we've narrowed down the range, i.e., start = end means start & end pointers point to the same number
        else:
            # So the guess number is either start or end pointers
            comp_guess = start
        # Recieve input from the user to run or exit the loop, h & l runs the loop with altered range, whereas c exits the loop, since the computer guessed the number
        user_feedback = input(f"Is {comp_guess} Too high (h) Too low (l), or correctly (c): ")
        # If user feedback says 'h', the number to be guessed is low and end pointer will be 1 less than current guess input 
        if user_feedback == 'h':
            end = comp_guess - 1
        # If user feedback says 'l', the number to be guessed is high and start pointer will be 1 more than current guess input 
        elif user_feedback == 'l':
            start = comp_guess + 1
    # Message when computer guessed it correct
    print(f"Yay, Awesome. You have guessed  the number {comp_guess} correctly")

# Calling the function with limit or range of values for the game
computer_guess(10)

