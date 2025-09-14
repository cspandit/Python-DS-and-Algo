"""Given an integer array arr[], the task is to count the number of subarrays in arr[] that are strictly increasing
and have a size of at least 2. A subarray is a contiguous sequence of elements from arr[]. A subarray is strictly increasing
if each element is greater than its previous element.
Examples:
Input: arr[] = [1, 4, 5, 3, 7, 9]
Output: 6"""

# O(n3)
def substring(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            flag = True
            for k in range(i, j):
                if arr[k] >= arr[k+1]:
                    flag = False
            if flag:
                count += 1
            else:
                break
    return count

# 0(n2)

def substring_better(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j-1] >= arr[j]:
                break
            else:
                count += 1
    return count


"""
Special sliding window O(n): 

1. Initialize a counter for the result => count = 0
2. Use a variable length to track the length of the current increasing subarray.
Iterate through the array: j = 1
3.If arr[j-1] < ar[j] : 
    a. increment length
    b. For every step where length ≥ 2, add length - 1 to the result.
4.Else, reset length to 1.

"""
def substring_best(arr):
    n = len(arr)
    count = 0
    length = 1
    j = 0
    while j < n:
        if arr[j-1] < arr[j]:
            length += 1
            count += length-1
        else:
            length = 1
        j += 1
    return count


A = [1, 4, 5, 3, 7, 9]
print(substring_better(A))