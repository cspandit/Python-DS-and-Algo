# Given a queue of integers of even length,
# rearrange the elements by interleaving the first half of the queue with the second half of the queue.
#
# Only a stack can be used as an auxiliary space.
#
# Examples:
#
# Input :  1 2 3 4
# Output : 1 3 2 4
#
# Input : 11 12 13 14 15 16 17 18 19 20
# Output : 11 16 12 17 13 18 14 19 15 20


class Queue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.items = [None]*capacity
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.items[self.rear] = data
            self.size += 1
            return
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = data
        self.size += 1

    def dequeue(self):
        temp = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front+1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.rear = -1
        return temp


def interleave(q):
    if q.size % 2 != 0:
        return
    mid = q.size//2
    stack = []
    while q.front < mid:
        stack.append(q.dequeue())

    while len(stack) > 0:
        q.enqueue(stack.pop())

    while q.front != 0:
        temp = q.dequeue()
        q.enqueue(temp)

    while q.front < mid:
        stack.append(q.dequeue())

    while len(stack) > 0:
        q.enqueue(stack.pop())
        temp = q.dequeue()
        q.enqueue(temp)


if __name__ == "__main__":
    queue = Queue(10)
    for i in range(11, 21):
        queue.enqueue(i)
    print(queue.items)
    interleave(queue)
    print(queue.items)
