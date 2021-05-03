from sys import maxsize


def max_sub_array(array, window_size, n):
    start = 0
    end = 0
    sm = 0
    max_sum = -maxsize
    while end < n:
        sm = sm + array[end]
        if end - start + 1 < window_size:
            end += 1

        elif end - start + 1 == window_size:
            max_sum = max(max_sum, sm)
            sm = sm - array[start]
            start += 1
            end += 1
    return max_sum


A = [2, 3, 5, 2, 9, 7, 1]
n = len(A)
print(max_sub_array(A, 3, n))
