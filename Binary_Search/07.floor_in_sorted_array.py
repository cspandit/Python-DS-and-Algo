# floor of an given number in sorted array is largest element smaller than given number.
# If given number is present in array then it should be considered.
# Idea is to find all smaller elements than given number and max of these is our answer.
# Same approach cab be applied to find ceiling i.e smallest element bigger than given number


def find_floor(array, key):
    low = 0
    high = len(array)-1
    res = -1  # taking any min value
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            res = max(res, array[mid])
            return res
        elif array[mid] > key:
            high = mid - 1
        else:
            res = max(res, array[mid])
            low = mid + 1

    return res


A = [1, 2, 3, 4, 8, 10, 12, 19]
floor = find_floor(A, 9)
print(floor)
