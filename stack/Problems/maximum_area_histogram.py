# Find the largest rectangular area possible in a given histogram(bar graph) where the largest rectangle can be made
# of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.
# link: https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

# This problem use the logic of finding two arrays of indexes of nearest smaller to right and nearest smaller to left
# every element. The difference b/w indexes of nearest smaller to right and nearest smaller to left minus 1 and
# multiplied by height of the bar gives one possible answer.
# This same very approach is used in stock span problem where we calculate a result vector containing index of nearest
# greater to left.


def max_area_histogram(array):
    right = nearest_smaller_to_right(array)
    left = nearest_smaller_to_left(array)
    result = []

    print("Right: ", right)
    print("Left: ", left)
    for i in range(len(array)):
        result.append((right[i] - left[i] - 1) * array[i])

    print("Result: ",result)
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


A = [6, 2, 5, 4, 5, 1, 6]
print(max_area_histogram(A))

