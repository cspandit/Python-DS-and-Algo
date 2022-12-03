# The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before
# given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
# then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
# link : https://www.geeksforgeeks.org/the-stock-span-problem/

# this problem is similar to nearest greater to left. Difference in indexes for current element and nearest greater
# to left gives total number the nearest consecutive smaller including element itself.
# Here result list will store index of nearest greater element to left instead of element itself and stack
# will store tuple of  nearest greater to left and its index.


def stock_span(array):
    n = len(array)
    stack = []
    res = []
    for i in range(n):
        if len(stack) == 0:
            res.append(-1)

        elif len(stack) > 0 and stack[-1][0] > array[i]:
            res.append(stack[-1][1])

        elif len(stack) > 0 and stack[-1][0] <= array[i]:
            while len(stack) > 0 and stack[-1][0] <= array[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            else:
                res.append(stack[-1][1])

        stack.append((array[i], i))
    print(res)
    for x in range(n):
        res[x] = x - res[x]

    return res


A = [100, 80, 60, 70, 60, 75, 85]
result = stock_span(A)
print(result)