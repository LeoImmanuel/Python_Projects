# Counting occurance specific character in a given word

def count_char(word:str, character:str)->int:
    count = 0
    for char in word.lower():
        if str(char) == str(character):
            count += 1
    return count

word = "Programming"
character = str(input(f"Enter the character to find occurance in {word}: "))
print(count_char(word, character))