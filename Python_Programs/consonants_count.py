# Counting CONSONANTS in a given word

def count_consonants(word:str)->int:
    vowels = ['a','e','i','o','u']
    count = 0
    for char in word.lower():
        if char not in vowels:
            count += 1
    return count

word = "Programming"
print(count_consonants(word))