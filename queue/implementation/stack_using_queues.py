class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity-1
        self.items = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return
        temp = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return temp


class Stack:
    def __init__(self):
        self.q1 = Queue(5)
        self.q2 = Queue(5)

    def __str__(self):
        s = ""
        for i in self.q1.items:
            s = s + str(i) + "->"
        return s[:-2]

    def push(self, data):
        self.q2.enqueue(data)

        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        temp = self.q1.dequeue()
        return temp


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
