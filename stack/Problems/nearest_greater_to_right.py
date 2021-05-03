# Problem is to print a result vector which will contain nearest greater element on right for all
# element of given array e.g [1,3,2,4] -> [3,4,4,-1]. If no greater is found insert -1
# Solution should be improvised version of O(n2) i.e. using stack

from queue import LifoQueue


def nearest_greater_using_std_library(array):
    n = len(array)
    stack = LifoQueue(n)
    res = []
    for i in range(n-1, -1, -1):
        if stack.qsize() == 0:
            res.append(-1)

        elif stack.qsize() > 0 and stack.queue[-1] > array[i]:
            res.append(stack.queue[-1])

        elif stack.qsize() > 0 and stack.queue[-1] <= array[i]:
            while stack.qsize() > 0 and stack.queue[-1] <= array[i]:
                stack.get()
            if stack.qsize() == 0:
                res.append(-1)
            else:
                res.append(stack.queue[-1])

        stack.put(array[i])
    return res


def nearest_greater_using_simple_list(array):
    n = (len(array))
    stack = []
    res = []
    for i in range(n-1, -1, -1):
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
result = nearest_greater_using_simple_list(A)
result.reverse()
print(result)
