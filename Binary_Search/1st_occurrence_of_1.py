# Problem is to find the 1st occurrence of 1 in infinite binary sorted array.
# This is combo of finding 1st occurrence of an element in sorted array and finding element in infinite sorted array


def first_occur(array, low, high):
    res = -1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == 1:
            res = mid
            high = mid-1
        elif array[mid] > 1:
            high = mid-1
        else:
            low = mid+1
    return res


def search(array):
    low = 0
    high = 1
    while array[high] < 1:
        low = high
        high = high*2

    return first_occur(array, low, high)


A = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
print(search(A))
