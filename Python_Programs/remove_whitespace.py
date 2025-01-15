# Removing Whitespaces in a string

def remove_whitespace(text):
    return "".join(char for char in text if char != " ")

text = "C O D E"
print(remove_whitespace(text))