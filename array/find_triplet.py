# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
# If there is such a triplet present in array, then print the triplet and return true. Else return false.
#
# Examples:
#
# Input: array = {12, 3, 4, 1, 9, 6}, sum = 24;
# Output: 12, 3, 9
# Explanation: There is a triplet (12, 3 and 9) present
# in the array whose sum is 24.


# Complexity O(n^3)
def find_triplet(array, sm):
    n = len(array)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if array[i] + array[j] + array[k] == sm:
                    print("Triplet is {0}, {1} and {2}".format(array[i], array[j], array[k]))
                    return True
    return False

# Complexity O(n^2)
def find_triplet_eff(array, sm):
    array.sort()
    n = len(array)
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if array[i] + array[l] + array[r] == sm:
                print("Triplet is {0}, {1} and {2}".format(array[i], array[l], array[r]))
                return True
            elif array[i] + array[l] + array[r] < sm:
                l += 1
            elif array[i] + array[l] + array[r] > sm:
                r -= 1
    return False


arr = [12, 3, 4, 1, 9, 6]
print(find_triplet_eff(arr, 24))
