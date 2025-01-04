# Find the Missing Number in a List
def find_missing_number(arr_list, n):
    complete_set = set(range(1,n+1))
    given_set = set(arr_list)
    return complete_set.difference(given_set)

# Test
print(find_missing_number([1, 2, 4, 5], 6))  # Output: 3