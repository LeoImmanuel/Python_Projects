# Checking for Palindrome
def is_palindrome(text):
    return bool(text.lower()==text.lower()[::-1])

text = 'kayaK'
print(is_palindrome(text))