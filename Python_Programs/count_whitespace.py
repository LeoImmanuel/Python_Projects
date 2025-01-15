# Counting whitespaces in a string
def count_whitespace(text):
    count = 0
    for char in text:
        if char == " ":
            count += 1
    return count

text = "Pr og ram mi ng"
# print(count_whitespace(text))

print(text.count(" "))
