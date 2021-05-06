# Problem is to reverse stack just using method push(), pop() and peek() and no extra space.
# We can recursively pop out all the elements hold it in stack then all the element are pushed one by one at bottom.
# To push element at bottom we can again use another recursive function which will 1st pop out all elements in stack,
# push the the incoming element and then push all popped out elements


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


def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)


def reverse_s(stack):
    if s.is_empty():
        return
    item = s.peek()
    s.pop()
    reverse_s(stack)
    insert_at_bottom(stack, item)


s = Stack()
for i in range(1, 6):
    s.push(i)
print(s)

reverse_s(s)
print(s)
