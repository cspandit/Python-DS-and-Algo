# This problem is similar to reversing stack using recursion.
# Here difference is only minimum element are pushed at bottom of stack


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


def insert_min(stack, item):
    if stack.is_empty() or stack.peek() < item:
        stack.push(item)
    else:
        temp = stack.pop()
        insert_min(stack, item)
        stack.push(temp)


def sort(stack):
    if s.is_empty():
        return
    item = s.peek()
    s.pop()
    sort(stack)
    insert_min(stack, item)


s = Stack()
s.push(2)
s.push(4)
s.push(1)
s.push(3)
print(s)

sort(s)
print(s)
