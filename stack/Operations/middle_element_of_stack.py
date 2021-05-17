# Problem is to find delete mid element of stack just by using pop() and push() and without using other data structure
# Idea is to pop recursively all the element and push back all except mid.


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        s_string = ""
        for i in self.items:
            s_string = s_string + str(i) + "->"
        return s_string[:-2]

    def push(self, data):
        self.items.append(data)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        return self.items.pop()


def delete_mid(s, n, cur):
    if s.is_empty():
        return
    x = s.peek()
    s.pop()
    delete_mid(s, n, cur+1)
    if cur != n//2:
        s.push(x)


stack = Stack()
for i in range(1, 7):
    stack.push(i)
print(stack)

delete_mid(stack, len(stack.items)-1, 0)
print(stack)