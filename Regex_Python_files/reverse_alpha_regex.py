import re

def reverse_non_digits(text:str)->str:
    formatted_string = ""
    extract_pattern = r'[a-z]+|\d+'
    alphanumerics = re.findall(extract_pattern, text)
    for word in alphanumerics:
        if word.isalpha():
            formatted_string += word[::-1]
        elif word.isdigit():
            formatted_string += word
    return formatted_string

text = "abc12asd2sjkls"
print(reverse_non_digits(text))



    