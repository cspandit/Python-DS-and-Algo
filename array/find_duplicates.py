# Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any
# number of times. Find these repeating numbers in O(n) and using only constant memory space.
#
# Example:
#
# Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
#
# Explanation: The numbers 1 , 3 and 6 appears more
# than once in the array.

# Complexity : O(n^2)
def find_duplicates(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                print(array[i], end=" ")


def find_duplicates_eff(array):
    for x in array:
        if array[abs(x)] > 0:
            array[abs(x)] = -1*array[abs(x)]
        else:
            print(abs(x), end=" ")


A = [1, 2, 3, 6, 3, 6, 1]
find_duplicates_eff(A)
