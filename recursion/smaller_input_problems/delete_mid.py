def delete_mid(stack, k):
    if k == 0:               # K holds mid index of given stack.
        stack.pop()
        return
    item = stack.pop()
    delete_mid(stack, k-1)
    stack.append(item)


A = [0, 1, 5, 2, 6]
delete_mid(A, len(A)//2)
print(A)
