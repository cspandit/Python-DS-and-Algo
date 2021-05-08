# Idea is to dequeue all the elements from queue and store in a stack then enqueue all elements from stack to queue
# Time complexity O(n) and Space complexity O(n)
# Files include iterative and recursion solution. Also include code to reverse 1st k elements in queue


class Queue:
    def __init__(self, capacity):
        self.items = [None]*capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.items[self.rear] = data
            self.size += 1
            return
        if not self.is_full():
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
        if self.size == 0:
            self.front = -1
            self.rear = -1
        return temp


def reverse_queue(qe):
    stack = []
    while qe.size > 0:
        stack.append(qe.dequeue())

    n = len(stack)
    while n > 0:
        qe.enqueue(stack.pop())
        n -= 1


def reverse_recur(qe, stack):
    if qe.size == 0:
        return
    stack.append(qe.dequeue())
    reverse_recur(qe, stack)
    qe.enqueue(stack.pop())


def reverse_first_k(qe, k):
    stack = []
    while k > 0:
        stack.append(qe.dequeue())
        k -= 1
    n = len(stack)
    while n > 0:
        qe.enqueue(stack.pop())
        n -= 1


if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.dequeue()
    q.enqueue(100)
    print(q.items)
