"""
Given an array arr[] of postive and negative integers, the objective is to find the number of subarrays having a sum
exactly equal to a given number k.
Examples:
Input : arr[] = [10, 2, -2, -20, 10], k = -10
Output : 3
"""

def largest_sum_subarray(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        sm = 0
        for j in range(i, n):
            sm += arr[j]
            if sm == k:
                count += 1
    print(count)


from collections import defaultdict
def largest_sum_subarray_efficient(arr, k):
    n = len(arr)
    d = defaultdict(int)
    sm = 0
    count = 0
    for i in range(n):
        sm += arr[i]

        if sm == k:
            count += 1
        if sm - k in d:
            count += d[sm-k]

        d[sm] += 1

    print(count)


arr = [10, 2, -2, -20, 10]
k = -10

largest_sum_subarray_efficient(arr, k)