import re

text = "abc12asd2sjkls"
get_extract_pattern = r'[a-z]+|\d+'

string_reverse = re.findall(get_extract_pattern, text)

reversed_string = ""

for match in string_reverse:
    if match.isalpha():
        reversed_string = reversed_string + match[::-1] 
    else:
        reversed_string = reversed_string + match

print(reversed_string)


    
