def prefix_to_postfix(exp):
    op = ["-", "+", "*", "/", "^"]
    stack = []
    for i in range(len(exp)-1, -1, -1):
        if exp[i] not in op:
            stack.append(exp[i])

        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + exp[i])

    print(stack[-1])


s = "*-A/BC-/AKL"
# output : ABC/-AK/L-*
prefix_to_postfix(s)