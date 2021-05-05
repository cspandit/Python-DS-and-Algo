# Problem is to find the element, which is having minimum difference with given key.
# Example: [1, 3, 8, 10, 15], key = 12 then answer is 10. If key is present in array then answer should be key its self
# as the minimum difference will be 0.
# This is nothing but simple binary search. At end of the search loop, just compare value at high and low index, min of
# these two will be ans if key is not present.


def find_min_difference(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid-1
        else:
            low = mid+1

    x = abs(array[high]-key)
    y = abs(array[low]-key)
    return array[high] if x < y else array[low]


A = [1, 3, 8, 10, 15]
print(find_min_difference(A, 12))