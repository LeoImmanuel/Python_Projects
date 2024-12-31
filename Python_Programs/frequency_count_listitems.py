from typing import List

def check_items_frequency(list_items:List[str])->dict:
    freq_dict = {}
    for item in list_items:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict

print(check_items_frequency(["apple","orange","grape","apple","watermelon","orange","apple"]))