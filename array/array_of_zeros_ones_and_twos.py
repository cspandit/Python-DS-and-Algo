# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array.
# The functions should put all 0s first, then all 1s and all 2s in last.
# Examples:
#
#
# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}


def sort_array(array):
    low = 0
    mid = 0
    high = len(array)-1
    while mid <= high:
        if array[mid] == 0:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        elif array[mid] == 1:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort_array(arr)
print(arr)

# Other approach will, run a for loop to count all the 0s, 1s and 2s and then run 3 separate loop to add them in array.
