# We can divide bitonic array into tow sorted array. Array from start to peak element[sorted in increasing order]
# and array from peak element to end[sorted in decreasing order]. After divide just call BS on both the array.


def binary_search_increasing(array, low, high, key):
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid-1
        else:
            low = mid+1
    return -1


def binary_search_decreasing(array, low, high, key):
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            low = mid+1
        else:
            high = mid-1
    return -1


def bitonic_search(array, key):
    low = 0
    n = len(array)
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid-1] < array[mid] > array[mid+1]:
            if key == array[mid]:
                return mid
            else:
                x = binary_search_increasing(array, 0, mid, key)
                y = binary_search_decreasing(array, mid+1, n-1, key)
                if x < 0 and y < 0:
                    return -1
                else:
                    return y if x < 0 else x

        elif array[mid] > array[mid-1]:
            low = mid+1
        else:
            high = mid-1


A = [1, 3, 8, 12, 4, 2]
print(bitonic_search(A, 4))
