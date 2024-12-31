def get_dict_frequency(dict_items:dict)->dict:
    dict_frequency = {}
    for val in dict_items.values():
        if val not in dict_frequency:
            dict_frequency[val] = 1
        else:
            dict_frequency[val] += 1
    return dict_frequency

def get_unique_dict_items(dict_items:dict)->dict:
    unique_dict_items = set()
    for val in dict_items.values():
        if val not in unique_dict_items:
            unique_dict_items.add(val)
    return unique_dict_items

dict_items = {'A':2000, 'B':2001, 'C':2002, 'D':2000}

print(get_dict_frequency(dict_items))
print(f"\n {get_unique_dict_items(dict_items)} ")