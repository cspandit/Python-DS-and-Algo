# Given an array of size n, find all elements in array that appear more than n/k times. For example,
# if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array
# is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that
# appear more than two times, 2 and 3.

from collections import defaultdict


# Approach sort and count the appearance.
def count_appear(array, k):
    array.sort()
    count = 1
    total_count = 0
    n = len(array)
    output = []
    for i in range(n-1):
        if array[i] == array[i+1]:
            count += 1
        elif count > n//k:
            total_count += 1
            output.append(array[i])
            count = 1
    if count > n//k:
        total_count += 1
        output.append(array[n-1])

    print(output)
    print(total_count)


# Using map
def count_appear_map(array, k):
    d = defaultdict(int)
    output = []
    n = len(array)
    count = 0
    for x in array:
        d[x] += 1

    for ky, v in d.items():
        if v > n//k:
            count += 1
            output.append(ky)

    print(output)
    print(count)


arr = [3, 1, 2, 2, 1, 2, 3, 3]
count_appear_map(arr, 4)
