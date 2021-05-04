# find last occurrence will have similar approach.
# Here we need to check right side of the array once kye is found


def find_first_occur(array, key):
    l = 0
    h = len(array) - 1
    res = -1
    while l <= h:
        mid = l + (h-l)//2
        if array[mid] == key:
            res = mid
            h = mid - 1

        elif array[mid] > key:
            h = mid - 1
        else:
            l = mid + 1
    return res


A = [2, 4, 10, 10, 10, 18, 20]
print(find_first_occur(A, 10))