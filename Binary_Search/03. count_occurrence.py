# As the array is sorted, occurrence will be consecutive.
# Idea is to find the 1st and last occurrences and then calculate difference b/w them.


def first_occur(array, key):
    """
        same code can be used to calculate both last and 1st occur, just need to use a flag to tell about
    """
    low = 0
    high = len(array) - 1
    res = -1
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == key:
            res = mid
            high = mid - 1
        elif array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return res


def last_occur(array, key):
    low = 0
    high = len(array) - 1
    res = -1
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == key:
            res = mid
            low = mid + 1
        elif array[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return res


def count_occur(array, key):
    f_occur = first_occur(array, key)
    l_occur = last_occur(array, key)

    return l_occur - f_occur + 1


A = [2, 4, 10, 10, 10, 18, 20]
print(count_occur(A, 10))
