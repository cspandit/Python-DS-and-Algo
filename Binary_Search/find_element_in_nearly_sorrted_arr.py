# Nearly sorted array is defined as an element which is supposed to be at index i could be at index i-1 or i or i+1
# Idea is each time we calculate mid, comparision is done with mid, mid-1 and mid+1 and also new high and low will be
# mid - 2 and mid + 2 respectively.


def search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high-low)//2
        if array[mid] == key:
            return mid
        elif mid-1 >= low and array[mid-1] == key:
            return mid-1
        elif mid + 1 <= high and array[mid+1] == key:
            return mid+1

        elif array[mid] > key:
            high = mid - 2
        else:
            low = mid + 2


A = [5, 10, 30, 20, 40]
print(search(A, 20))
