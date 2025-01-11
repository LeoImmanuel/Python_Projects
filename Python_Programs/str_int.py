# Given a string, the task is to convert the string into an integer
# Input: "Three hundred million"
# Output: 300000000
# Input1: "Five Hundred Thousand"
# Output1: 500000


def words_to_number(text):
    values_dict = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10, "hundred": 100,
        "thousand": 1000, "million": 1000000
    }
    words = text.lower().split()
    result = 0
    curr = 0

    for word in words:
        if word in values_dict:
            num = values_dict[word]
            if num == 100:
                curr *= num
            elif num >= 1000:
                curr *= num
                result += curr
                curr = 0
            else:
                curr += num
    
    result += curr
    return result

text = "Three hundred million"
print(words_to_number(text))



    