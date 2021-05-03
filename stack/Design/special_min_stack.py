# Question is to design a special stack which give minimum in O(1) at any point,
# given that all other operations on stack is standard.


class Node:
    def __init__(self, value):
        self.value = value
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
            string += str(temp.value) + "->"
            temp = temp.next

        return string[:-2]

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def peek(self):
        return self.head.value

    def pop(self):
        remove = self.head.value
        self.head = self.head.next
        return remove

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size


class SpecialStack(Stack):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.min_stack = Stack(max_size)

    def push(self, value):
        if self.is_empty():
            super().push(value)
            self.min_stack.push(value)
        else:
            temp = self.min_stack.peek()
            if value < temp:
                self.min_stack.push(value)
                super().push(value)
            else:
                self.min_stack.push(temp)
                super().push(value)

    def pop(self):
        x = super().pop()
        self.min_stack.pop()
        return x

    def get_min(self):
        return self.min_stack.peek()


if __name__ == "__main__":
    stack = SpecialStack(5)
    stack.push(18)
    stack.push(19)
    stack.push(29)
    stack.push(15)
    stack.push(16)

    print(stack)
    print("MIN: ", stack.get_min())

    print(stack.pop())
    print(stack.pop())

    print(stack)
    print("min: ", stack.get_min())

