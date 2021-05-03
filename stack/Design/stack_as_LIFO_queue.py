from queue import LifoQueue

stack = LifoQueue(3)
print(stack.empty())

stack.put("a")
stack.put("b")
stack.put("c")

print(stack.queue[-1])

print(stack.full())
print(stack.get())
print(stack.get())
print(stack.get())

print(stack.qsize())

