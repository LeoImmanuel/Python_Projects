import re

def sumPair_BTW_question_marks(text:str)->bool:
    extract_digits = r'(\d)\?{3}(\d)'
    pair_of_digits = re.findall(extract_digits, text)
    for digits in pair_of_digits:
        if int(digits[0]) + int(digits[1]) == 10:
            return True
    return False 

text = 'as3??4sad5???5werw5???4sdf'
print(sumPair_BTW_question_marks(text))