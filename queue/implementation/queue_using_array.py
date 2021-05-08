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
        if not self.is_full():
            self.rear = (self.rear+1) % self.capacity
            self.items[self.rear] = data
            self.size += 1
        else:
            raise Exception("Overflow")

    def dequeue(self):
        if not self.is_empty():
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front+1) % self.capacity
            self.size -= 1
            return temp
        else:
            raise Exception("Underflow")

    def q_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.items[self.front]

    def q_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.items[self.rear]


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.items)
print(q.q_front())
print(q.q_rear())
print(q.dequeue())
print(q.items)
print(q.q_front())
print(q.q_rear())
print(q.size)
