# Counting VOWELS in a given word

def count_vowels(word:str)->int:
    vowels = ['a','e','i','o','u']
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

word = "Programming"
print(count_vowels(word))