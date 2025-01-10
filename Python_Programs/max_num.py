# Finding maximum number in the list

def find_max(num_list):
    max = num_list[0]
    for num in num_list:
        if max < num:
            max = num
    return max

num_list = [12,3,55,23,6,78,33,4]
print(find_max(num_list))