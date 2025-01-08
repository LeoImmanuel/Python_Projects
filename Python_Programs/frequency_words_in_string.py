# Count the Frequency of Words in a String

from collections import Counter

def word_frequency(string: str)->dict:
    word_frequency_in_string = {}
    for word in string.split():
        if word not in word_frequency_in_string:
            word_frequency_in_string[word] = 1
        else:
            word_frequency_in_string[word] += 1
    return word_frequency_in_string

def word_frequency_counter(string: str)->dict:
    return Counter(string.split())

# Test
print(word_frequency("the cat in the hat"))  # Output: Counter({'the': 2, 'cat': 1, 'in': 1, 'hat': 1})

# print(word_frequency_counter("the cat in the hat the cat")) 