# Given an array arr[] and size of array is n and one another key x, and give you a segment size k. The task is to
# find that the key x present in every segment of size k in arr[].
# If size of array is not equally divisible by k then the last segment will not have of size k.

def check_key(array, x, k, n):
    i = 0
    while i < n:
        if i + k < n:
            j = 0
            while j < k:
                if array[i+j] == x:
                    break
                j += 1
            if j == k:
                return False
        i = i+k
    if i == n:
        return True
    j = i - k
    while j < n:
        if array[j] == x:
            break
        j += 1

    if j == n:
        return False
    return True


A = arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3, 0, 3]

print(check_key(A, 3, 3, len(A)))