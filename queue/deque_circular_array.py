# There are 4 methods:
# Lets assume at start front = rear = -1 and for first insert both front and rear is at index 0
# 1. insertFront() -> pointer moves in backward direction. Make sure when front is at index 0 then for next insert it
                        # point to n-1(if front==0: front=n-1 )
# 2. deleteFront() -> pointer moves in forward direction.(front = front+1 % n)
# 3. insertRear() -> pointer moves in forward direction. (rear = rear+1 % n)
# 4. deleteRear() -> pointer moves in backward direction. Make sure when front is at index 0 then for next insert it
                        # point to n-1(if rear==0: rear = n-1 )
# deque full conditions are : front = rear + 1 or front==0 and rear = n-1


class Deque:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.items = [None]*capacity
        self.capacity = capacity

    def is_empty(self):
        if self.front == -1 and self.rear == -1:
            return True

    def is_full(self):
        if self.front == self.rear+1 or (self.rear == self.capacity-1 and self.front == 0):
            return True

    def enqueue_front(self, data):
        if self.is_full():
            raise Exception("Deque Full")
        elif self.is_empty():
            self.rear = 0
            self.front = 0
            self.items[self.front] = data
        elif self.front == 0:
            self.front = self.capacity-1
            self.items[self.front] = data
        else:
            self.front -= 1
            self.items[self.front] = data

    def enqueue_rear(self, data):
        if self.is_full():
            raise Exception("Deque Full")
        elif self.is_empty():
            self.rear = 0
            self.front = 0
            self.items[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.capacity
            self.items[self.rear] = data

    def dequeue_front(self):
        if self.is_empty():
            raise Exception("Deque Empty")
        elif self.rear == self.front:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front+1) % self.capacity
            return temp

    def dequeue_rear(self):
        if self.is_empty():
            raise Exception("Deque Empty")
        elif self.rear == self.front:
            temp = self.items[self.rear]
            self.items[self.rear] = None
            self.front = -1
            self.rear = -1
            return temp
        elif self.rear == 0:
            temp = self.items[self.rear]
            self.items[self.rear] = None
            self.rear = self.capacity-1
            return temp
        else:
            temp = self.items[self.rear]
            self.items[self.rear] = None
            self.rear -= 1
            return temp

    def get_front(self):
        return self.items[self.front]

    def get_rear(self):
        return self.items[self.rear]


d = Deque(5)
d.enqueue_front(1)
d.enqueue_front(2)
d.enqueue_rear(3)
d.enqueue_rear(4)
d.enqueue_rear(5)
print(d.items)
print("Front : ", d.get_front())
print("Rear : ", d.get_rear())
print(d.dequeue_rear())
print(d.dequeue_front())
print(d.dequeue_front())
print(d.items)
