# Given an array that contains both positive and negative integers, find the product of the maximum product subarray
# Input: arr[] = {6, -3, -10, 0, 2}
# Output:   180  // The subarray is {6, -3, -10}
#
# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60  // The subarray is {60}

# Brute Force
def largest_product(array):
    max_product = array[0]
    n = len(array)
    for i in range(n):
        prod = array[i]
        for j in range(i+1, n):
            max_product = max(prod, max_product)
            prod = prod*array[j]
    return max_product

def largest_product_kadane(array):
    max_ending = 1
    max_so_far = -1000
    for x in array:
        max_ending = max_ending*x
        if max_so_far < max_ending:
            max_so_far = max_ending
        if max_ending == 0:
            max_ending = 1
    return max_so_far


A = [0, 0, 1, 0]
print(largest_product_kadane(A))
