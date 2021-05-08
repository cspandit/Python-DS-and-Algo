class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        s = str(self.front.data)
        temp = self.front.next
        while temp != self.front:
            s = s + "->" + str(temp.data) + "->"
            temp = temp.next
        s = s + "Front"
        return s

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
        else:
            self.rear.next = new_node

        self.rear = new_node
        self.rear.next = self.front

    def dequeue(self):
        if self.front is None and self.rear is None:
            return
        if self.rear is self.front:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.data

        temp = self.front
        self.front = temp.next
        self.rear.next = self.front
        return temp.data


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q)