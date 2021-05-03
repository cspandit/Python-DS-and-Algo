class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, max_size):
        self.head = None
        self.size = 0
        self.max_size = max_size

    def __str__(self):
        temp = self.head
        string = ""
        while temp:
            string += str(temp.data) + "->"
            temp = temp.next
        return string[:-2]

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise Exception("Trying to pop out of empty stack")
        remove = self.head.data
        self.head = self.head.next
        return remove

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


if __name__ == "__main__":
    stack = Stack(10)
    print(stack.is_empty())
    for i in range(10):
        stack.push(i)

    print(stack.is_full())
    print(stack.peek())
    print(stack)
    for i in range(10):
        print(stack.pop())

    print(stack.is_empty())
