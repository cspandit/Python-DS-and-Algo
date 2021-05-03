def largest_sub(array, k, n):
    max_size = -1
    start = 0
    end = 0
    sm = 0
    while end < n:
        sm = sm + array[end]
        if sm < k:
            end += 1

        elif sm == k:
            max_size = max(max_size, end-start+1)
            end += 1

        else:
            while sm > k:
                sm = sm - array[start]
                start += 1
            end += 1

    return max_size


# Only for array with +ve elements
A = [4, 1, 1, 1, 2, 3, 5]
n = len(A)
print(largest_sub(A, 5, n))
