from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("Stack: ", stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack: ", stack)


