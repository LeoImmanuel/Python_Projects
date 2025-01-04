# Find Duplicates in a List
from typing import List

def find_duplicates(arr_list: List[int])->List[int]:
    seen = set()
    duplicate = []
    for num in arr_list:
        if num in seen:
            duplicate.append(num)
        seen.add(num)
    return duplicate

# Test
print(find_duplicates([1, 2, 3, 1, 2, 4]))  # Output: [1, 2]