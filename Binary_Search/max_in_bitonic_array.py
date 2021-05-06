# Bitonic Array is one which increases monotonically and then decrease monotonically.
# Monotonic increase means element at index  i+1 will always be greater than ith element
# Example : [1, 3, 8, 12, 4, 2] - here array goes monotonically then decrease similarly.
# This problem is similar to peak element problem, here there will be just one peak element. like 12 in above example.


def bitonic_max(array):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid-1] < array[mid] > array[mid+1]:
            return array[mid]
        elif array[mid] > array[mid-1]:
            low = mid+1
        else:
            high = mid-1


A = [1, 3, 8, 12, 4, 2]
print(bitonic_max(A))
