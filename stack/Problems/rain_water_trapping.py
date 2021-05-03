# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.

# Examples:

# Input: arr[]   = {2, 0, 2}
# Output: 2


def rain_trapped_brute_force(array):
    res = 0
    n = len(array)
    for i in range(n):
        lmax = array[i]

        for j in range(i, -1, -1):
            lmax = max(lmax, array[j])

        rmax = array[i]
        for k in range(i+1, n):
            rmax = max(rmax, array[k])

        res = res + min(lmax, rmax) - array[i]

    return res


def rain_trapped_extra_space(array):
    n = len(array)
    lmax = [array[0]]
    rmax = [array[n-1]]
    res = 0
    for i in range(1, n):
        lmax.append(max(array[i], lmax[-1]))

    for j in range(n-2, -1, -1):
        rmax.append(max(array[j+1], rmax[-1]))
    rmax.reverse()

    for i in range(n):
        res = res + min(lmax[i], rmax[i]) - array[i]

    return res


def rain_trapped_efficient(array):
    l = 0
    h = len(array) - 1
    lmax = array[l]
    rmax = array[h]
    res = 0
    while l < h:
        if array[h] < array[l]:
            rmax = max(rmax, array[h])
            res = res + min(lmax, rmax) - array[h]
            h -= 1
        else:
            lmax = max(lmax, array[l])
            res = res + min(lmax, rmax) - array[l]
            l += 1

    return res


def rain_trapped_stack(array):
    """
    Idea is traverse the given array and push the index till current height is smaller than
        the the height indicated by index at top of stack. if greater height is found:
        1. pop top of stack and store in temp variable
        2. calculate distance current_index - stack_top -1
        3. Calculate bounded_height = min(height(current), height(stack_top)) - height[temp]
        4. Calculate ans = ans + bounded_height * distance
    At last push index of current height to stack
    """
    stack = []
    res = 0
    for i in range(len(array)):
        while len(stack) > 0 and array[i] > array[stack[-1]]:
            top = stack.pop()
            # If this is popping the only element in stack, then dis = i - stack[-1] - 1 can cause error
            if len(stack) == 0:
                break
            dis = i - stack[-1] - 1
            height = min(array[i], array[stack[-1]]) - array[top]
            res = res + (height * dis)
        stack.append(i)
    return res


A = [3, 0, 2, 0, 4]
print("Max trapped rain: ", rain_trapped_stack(A))