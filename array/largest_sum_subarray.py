# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers that has
# the largest sum.

# Brute force: find all the sub array and look for max sum
def largest_sum(array):
    max_sum = array[0]
    n = len(array)
    for i in range(n):
        sm = array[i]
        for j in range(i+1, n):
            max_sum = max(sm, max_sum)
            sm = sm+array[j]
    return max_sum

# Complexity : O(n)
def largest_sum_kadane(array):
    max_ending = 0
    max_so_far = 0
    for x in array:
        max_ending += x
        if max_so_far < max_ending:
            max_so_far = max_ending
        if max_ending < 0:
            max_ending = 0

    return max_so_far


A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(largest_sum(A))
