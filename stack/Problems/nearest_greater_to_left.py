# Problem is to print a result vector which will contain nearest greater element on left for all
# element of given array e.g [1,3,2,4] -> [-1,-1,3,-1]. If no greater is found insert -1
# Solution should be improvised version of O(n2) i.e. using stack


def nearest_greater_left(array):
    n = len(array)
    stack = []
    res = []
    for i in range(n):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1] > array[i]:
            res.append(stack[-1])

        elif len(stack) > 0 and stack[-1] <= array[i]:
            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1])

        stack.append(array[i])
    return res


A = [1, 3, 2, 4]
result = nearest_greater_left(A)
# result.reverse() :: No reverse is required
print(result)