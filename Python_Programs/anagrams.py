# Comparing Two strings for Anagrams
def is_anagram(str1,str2):
    return bool(sorted(str1.replace(" ","").lower()) == sorted(str2.replace(" ","").lower()))

str1 = 'Listen'
str2 = 'Silent'
print(is_anagram(str1,str2))