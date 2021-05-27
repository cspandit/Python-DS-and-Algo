def max_one(matrix):
    max_count = 0
    for x in matrix:
        low = 0
        high = 1
        while x[high] < 1:
            low = high
            high = high*2
            if high >= len(x):
                high = len(x)-1
                # if array only contain 0s this will break the loop
                break
        first = first_occur(x, low, high)
        # if 1 is not present in array return will be -1
        if first != -1:
            count = len(x) - first
            max_count = max(max_count, count)
    return max_count

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


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

print(max_one(mat))