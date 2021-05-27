# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are
# consecutive integers, the consecutive numbers can be in any order.
#
# Examples:
#
# Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
# Output: 4
# Explanation:
# The subsequence 1, 3, 4, 2 is the longest
# subsequence of consecutive elements
#
# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
# Output: 5
# Explanation:
# The subsequence 36, 35, 33, 34, 32 is the longest
# subsequence of consecutive elements.

# Approach :
# The idea is to first sort the array and find the longest subarray with consecutive elements.
# After sorting the array and removing the multiple occurrences of elements initialize variable count and max_count
# with 1.if A[i]+1 == A[i+1] then increase count and calculate max_count else make count 1 as new subsequence will start

# Complexity : O(nlogn)
def longest_subsequence(array):
    array.sort()
    array = remove_duplicates(array)
    count = 1
    max_count = 1
    for i in range(len(array)-1):
        if array[i] + 1 == array[i+1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)
    return max_count

def remove_duplicates(array):
    n = len(array)
    j = 0
    for i in range(n-1):
        if array[i] != array[i+1]:
            array[j] = array[i]
            j += 1
    array[j] = array[n-1]
    return array[:j+1]


arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
print(longest_subsequence(arr))

