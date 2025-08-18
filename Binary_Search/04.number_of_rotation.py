# Problem is to find number of rotation for given  sorted rotated array
# [11, 12, 15, 18, 2, 5, 6, 8] -> output : 4
# Original array before rotation would have been [2, 5, 6, 8, 11, 12, 15, 18]
# There few observation about sorted array:
# 1. if 1st element is smaller than last than array has zero rotation.
# 2. any element which is smaller than elements on its either sides is considered to min element in array
# 3. Index of min element is exactly equal to the number of rotation.
# 4. When rotated array is divided from mid, one of the resultant array is always unsorted array and it will contain min


def rotation_number(array):
    low = 0
    n = len(array)
    high = n - 1

    while low <= high:
        if array[low] < array[high]:
            return low
        mid = low + (high - low)//2
        # the reason of doing modulo is that when mid is last or 1st, mid+1 or mid-1 should not result out of index
        nex = (mid + 1) % n
        pre = (mid + n - 1) % n
        if array[mid] < array[nex] and array[mid] < array[pre]:
            return mid

        elif array[low] <= array[low]:
            low = mid+1
        elif array[mid] <= array[high]:
            high = mid - 1


# A = [8, 11, 12, 15, 18, 2, 5, 6]
A = [5, 6, 8, 11, 12, 15, 18, 2]
print(rotation_number(A))


