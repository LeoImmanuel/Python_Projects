# Finding minimum number in the list

def find_min(num_list):
    min = num_list[0]
    for num in num_list:
        if min > num:
            min = num
    return min

num_list = [12,3,55,23,6,78,33,4]
print(find_min(num_list))