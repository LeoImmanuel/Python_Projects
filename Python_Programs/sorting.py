def Bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def Selection_Sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def Insertion_Sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        Merge_Sort(left_arr)
        Merge_Sort(right_arr)

        i=j=k=0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [ item for item in arr if item < pivot ]
        middle = [item for item in arr if item == pivot]
        right = [ item for item in arr if item > pivot ]
    return Quick_Sort(left) + middle + Quick_Sort(right)


arr_list = [ 5, 1, 8, 55, 27, 77, 11, 3, 7, 13, 2, 43, 11 ]
print("Before Sorting the array list:",arr_list)

"""
Bubble_Sort(arr_list)
print("Bubble Sort", arr_list)

Selection_Sort(arr_list)
print("Selection Sort", arr_list)

Insertion_Sort(arr_list)
print("Insertion Sort", arr_list)
"""

Merge_Sort(arr_list)
print("Merge Sort", arr_list)

"""
Sorted = Quick_Sort(arr_list)
print("Quick Sort", Sorted)
"""
