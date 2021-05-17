# Example 1:
# Input: "(()())(())"
# Output: "()()()"

# Example 2:
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"


s = "(()())(())(()(()))"


def remove_pran(string):
    bal = 0
    stack = []
    res = ''
    for p in string:
        if p == '(':
            bal += 1
        else:
            bal -= 1

        stack.append(p)
        if bal == 0:
            stack.pop(0)
            stack.pop(-1)
            res = res + "".join(stack)
            stack = []
    return res


print(remove_pran(s))
