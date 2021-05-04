# This problem is continuation of number of rotation in sorted array.
# Idea is after we find min element, we have sorted array on either side of min element.
# After this we just need to call BS function on both sorted array.


def binary_search(array, low, high, key):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == key:
            return mid

        elif array[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    return -1


def find_min_index(array):
    n = len(array)
    low = 0
    high = n - 1
    while low <= high:
        if array[low] < array[high]:
            return low
        mid = low + (high - low)//2
        pre = array[mid-1]
        nex = array[mid+1]
        if array[mid] < pre and array[mid] < nex:
            return mid
        elif array[low] < array[mid]:
            low = mid + 1
        elif array[mid] < array[high]:
            high = mid - 1


def find_element(array, key):
    min_index = find_min_index(array)
    x = binary_search(array, 0, min_index-1, key)
    y = binary_search(array, min_index, len(array)-1, key)

    if x == -1 and y == -1:
        return -1
    elif x > -1:
        return x
    else:
        return y


A = [11, 12, 15, 18, 2, 5, 6, 8]
print(find_element(A, 6))

