# linked list implementation of queue has enqueue and dequeue operations in time O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        temp = self.front
        s = ""
        while temp:
            s = s + str(temp.data) + "->"
            temp = temp.next
        return s[:-2]

    def is_empty(self):
        if self.front is None and self.rear is  None:
            return True
        else:
            return False

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data


q = Queue()
for i in range(3):
    q.enqueue(i)

print(q)
print(q.dequeue())
print(q)
