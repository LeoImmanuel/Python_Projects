# Reverse a String Without Using Built-In Functions

def reverse_string(string: str)->str:
    rev_str = ""
    for word in string:
        rev_str = word + rev_str
    return rev_str

def reverse_string_use_slice(string: str)->str:
    return string[::-1]

# Test 
# print(reverse_string("Interview"))

print(reverse_string_use_slice("Interview round"))