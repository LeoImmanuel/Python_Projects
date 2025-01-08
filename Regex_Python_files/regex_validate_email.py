# Regular Expression: Validate Email Address

import re

def validate_email(string:str)->bool:
    pattern = r'^[a-zA-Z0-9-.+_]+\@[a-zA-Z]+\.[a-zA-Z]{2,3}$'
    return bool(re.match(pattern, string)) 

# Test
print(validate_email("example@domain.com"))  # Output: True
print(validate_email("example.com"))        # Output: False