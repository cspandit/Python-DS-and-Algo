# Problem is to implement stack in such a way that it returns min of stack in O(1) and space O(1)
# Idea is to store tuple of element and current min in stack.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        temp = self.head
        res = ""
        while temp:
            res = res + str(temp.data[0]) + "->"
            temp = temp.next

        return res[:-2]

    def is_empty(self):
        if self.head is None:
            return True

    def push(self, data):
        if self.head is None:
            new_node = Node((data, data))
        else:
            if data >= self.head.data[1]:
                data = (data, self.head.data[1])
            else:
                data = (data, data)
            new_node = Node(data)
            new_node.next = self.head

        self.head = new_node

    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next

    def get_min(self):
        return self.head.data[-1]


A = [18, 19, 29, 15, 16]
stack = Stack()
for i in A:
    stack.push(i)
print(stack)
print(stack.get_min())
stack.pop()
stack.pop()
print(stack)
print(stack.get_min())