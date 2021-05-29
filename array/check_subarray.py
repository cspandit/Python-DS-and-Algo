# Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not.
# Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.
#
# Examples:
#
# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]
#
# Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
# Output: arr2[] is a subset of arr1[]

# Brute Force O(n^2)
def check_subarray(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    for i in range(n2):
        j = 0
        while j < n1:
            if arr1[j] == arr2[i]:
                break
            j += 1
        if j == n1:
            return False
    return True

# Using Binary search on sorted array O(nlogn)
def check_subarray_bs(arr1, arr2):
    arr1.sort()
    for x in arr2:
        res = binary_search(arr1, x)
        if not res:
            return False
    return True

def binary_search(arr, key):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = l + (h-l)//2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            h = mid-1
        else:
            l = mid+1
    return False


A = [11, 1, 13, 21, 3, 7]
B = [11, 3, 7, 2]

print(check_subarray_bs(A, B))
