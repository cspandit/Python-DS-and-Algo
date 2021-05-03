# Design stack to perform operations, getMid(), add_mid(), del_mid() in O(1)
import gc


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.mid = None

    def __str__(self):
        temp = self.top
        string = ""
        while temp:
            string += str(temp.data) + "<=>"
            temp = temp.next
        return string[:-3]

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.count += 1

        if self.count == 1:
            self.mid = new_node
        else:
            self.top.prev = new_node
            if self.count % 2 != 0:
                self.mid = self.mid.prev

        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack Underflow")

        temp = self.top
        self.top = self.top.next
        self.top.prev = None
        self.count -= 1
        if self.count % 2 == 0:
            self.mid = self.mid.next

        return temp.data

    def add_mid(self, data):
        new_node = Node(data)
        temp = self.mid
        new_node.next = self.mid
        new_node.prev = self.mid.prev
        self.mid.prev.next = new_node
        self.mid.prev = new_node
        self.count += 1

        if self.count % 2 != 0:
            self.mid = self.temp.prev

    def del_mid(self):
        if self.mid is None or self.mid.next is None or self.mid.prev is None:
            return
        temp = self.mid
        self.mid.next.prev = self.mid.prev
        self.mid.prev.next = self.mid.next
        self.count -= 1
        if self.count % 2 == 0:
            self.mid = temp.next
        else:
            self.mid = temp.prev


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.push(5)
    print(stack)
    print(stack.mid.data)
    stack.del_mid()
    print(stack)
    print(stack.mid.data)

    stack.del_mid()
    print(stack)
    print(stack.mid.data)

    stack.del_mid()
    print(stack)
    print(stack.mid.data)