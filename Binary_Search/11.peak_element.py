# Element which is greater than both its neighbor is peak element. For boundary element(at index 0 or size-1)
# to become peak element, it should be just greater than its one available neighbor.
# There can be just more than one peak elements in given array, in that case we just need to return any one of those.
# Example : [5, 10, 20, 15] -> peak element is 20
# Example : [10, 20, 15, 2, 23, 90, 67] -> 20 and 90 are peak element
# Example : [23, 1, 0] -> 23 at index 0 is peak element
# This question is based on concept called Binary search on answer. Here criteria to move on either side of array is
# depends on type of problem.(Note that in standard BS it was decided by comparing key with mid element)


def peak_element_index(array):
    low = 0
    n = len(array)
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        # to make sure mid is not boundary element
        if 0 < mid < n-1:
            if array[mid-1] < array[mid] > array[mid+1]:
                return mid
            # so the criteria is, if mid element is greater than its left neighbor possibility of finding peak element
            # on immediate left of mid is not there so move on right side of array.
            elif array[mid] > array[mid-1]:
                low = mid+1
            else:
                high = mid-1
        # In case mid is boundary element
        elif mid == 0:
            if array[0] > array[1]:
                return 0
            else:
                return 1
        else:
            if array[mid] > array[n-2]:
                return n-1
            else:
                return n-2


A = [5, 10, 20, 15]
print(peak_element_index(A))

