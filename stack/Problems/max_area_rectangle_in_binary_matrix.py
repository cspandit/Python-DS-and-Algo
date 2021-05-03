# Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s.
# This problem is similar to max area histogram. Here each row summed up with its all previous row is one problem.
# i.e MAH1 = MAH(row1)
#     MAH2 = MAH(row1 + row2)
#     MAH2 = MAH(row1 + row2 + row3)
#     MAH2 = MAH(row1 + row2 + row3 + row4)-> (if element of base row is 0 while adding rows then that element become 0)
# Now the solution to this problem is max(MAH1, MAH2, MAH3, MAH4)
# Link: https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/


def max_area_rectangle(binary_matrix):
    mah_results = []
    heights = [0]*len(binary_matrix[0])
    for i in binary_matrix:
        for j in range(len(i)):
            if i[j] != 0:
                heights[j] = heights[j] + i[j]
            else:
                heights[j] = 0

        mah_results.append(max_area_histogram(heights))

    return max(mah_results)


def max_area_histogram(array):
    right = nearest_smaller_to_right(array)
    left = nearest_smaller_to_left(array)
    result = []

    for i in range(len(array)):
        result.append((right[i] - left[i] - 1) * array[i])

    return max(result)


def nearest_smaller_to_right(array):
    n = len(array)
    stack = []
    res = []
    for i in range(n-1, -1, -1):
        if len(stack) == 0:
            res.append(len(array))

        elif len(stack) > 0 and stack[-1][0] < array[i]:
            res.append(stack[-1][1])

        elif len(stack) > 0 and stack[-1][0] >= array[i]:
            while len(stack) > 0 and stack[-1][0] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(len(array))
            else:
                res.append(stack[-1][1])

        stack.append((array[i], i))

    res.reverse()
    return res


def nearest_smaller_to_left(array):
    n = len(array)
    stack = []
    res = []
    for i in range(n):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1][0] < array[i]:
            res.append(stack[-1][1])

        elif len(stack) > 0 and stack[-1][0] >= array[i]:
            while len(stack) > 0 and stack[-1][0] >= array[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1][1])
        stack.append((array[i], i))

    return res


A = [[0, 1, 1, 0],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 0, 0]]

print(max_area_rectangle(A))