# In case of infinite sorted array we assume end index is not available.
# We assume 0 as start index and 1 as last index. if


def binary_search(array, low, high, key):
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            high = mid-1
        else:
            low = mid+1


def search(array, key):
    low = 0
    high = 1
    while array[high] < key:
        low = high
        high = high*2
    return binary_search(array, low, high, key)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(search(A, 8))
