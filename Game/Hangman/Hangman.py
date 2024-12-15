import random
import string
from hangman_words import words

# Function to get a word from the words list
def get_valid_word(words):
    # Randomly choice something from that list
    word = random.choice(words)
    # If word is '-' or ' ' get a new word 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    # Keeping track of letters in the word 
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    # Keep track of the letters user has guessed 
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0 :
        # Letters used. ' '.join(['a','b','c']) --> 'a b c'
        print(f'You"'"ve", lives, 'lives left and you have used these letters:',''.join(used_letters))

        # Tell user what the current word is (i.e., W - R D )
        word_list = [ letter if letter in used_letters else '-' for letter in word ]
        print("Current word: ",' '.join(word_list))

        # Getting user input and convert it to uppercase letter
        user_letter = input('Guess a letter: ').upper()
       
        # If User input that I haven't used yet i.e., present in alphabet
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            # Check is the user input is present in word to be guessed 
         
            if user_letter in word_letters:
                # Remove user letter from the word_letters 
                word_letters.remove(user_letter)
        
            else:
                # Takes away life
                lives -= 1
                print("Letter is not in word")

        # If user input present in used letters
        elif user_letter in used_letters:
            print("You've already guessed that letter. Please try again..")

        # User input not in alphabet or used letters
        else:
            print("Invalid Input. Please try again..")

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print("You guessed the word", word,"!!")

hangman()