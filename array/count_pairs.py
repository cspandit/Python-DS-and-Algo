# Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal
# to ‘sum’.
#
# Examples:
#
# Input  :  arr[] = {1, 5, 7, -1},
# sum = 6
# Output :  2
from collections import defaultdict

# Complexity : O(n^2)
def count_pairs(array, s):
    count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == s:
                count += 1
    return count

# Complexity : O(n) : Using map
def count_pairs_map(arr, sm):
    d = defaultdict(int)
    twice_count = 0
    for x in arr:
        d[x] += 1

    for x in arr:
        twice_count += d[sm - x]
        if sm - x == x:
            twice_count -= 1

    return twice_count//2


A = [1, 5, 7, -1, 3]
print(count_pairs_map(A, 6))

