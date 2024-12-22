from Sorting import Merge_Sort

def Binary_Search(arr,n):
    if len(arr) <= 0:
        return False
    else:
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high) // 2

            if arr[mid] == n:
                globals()['pos'] = mid
                return True
            elif n > arr[mid]:
                low = mid + 1
            else:
                high = mid -1

    return False


def Linear_Search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            globals()['pos'] = i
            return True

    return False

unsorted_arr_list = [ 5, 1, 8, 3, 7, 13, 2, 43, 11 ]
element_to_searched = 11

#found = Linear_Search(unsorted_arr_list,element_to_searched)
sorted_arr = Merge_Sort(unsorted_arr_list)
found = Binary_Search(sorted_arr,element_to_searched)

if found:
    print(f"Element {element_to_searched} is found at position:",pos+1)
else:
    print(f"Element {element_to_searched} is not found in the array of elements")