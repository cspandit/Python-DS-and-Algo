# For implementing deque, we need to keep track of two pointers, front and rear.
# We enqueue (push) an item at the rear or the front end of deque and dequeue(pop) an item from both rear and front end.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        temp = self.front
        s = "front->"
        while temp:
            s = s + str(temp.data) + "<=>"
            temp = temp.next
        s = s[:-3] + "<-rear"
        return s

    def enqueue_front(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return

        self.front.prev = new_node
        new_node.next = self.front
        self.front = new_node

    def enqueue_rear(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        new_node.prev = self.rear
        self.rear.next = new_node
        self.rear = new_node

    def delete_front(self):
        if self.front is None:
            return
        if self.front is self.rear:
            self.rear = None
            self.front = None
            return
        self.front = self.front.next
        self.front.prev = None

    def delete_rear(self):
        if self.rear is None:
            return
        if self.rear is self.front:
            self.front = None
            self.rear = None
        self.rear = self.rear.prev
        self.rear.next = None

    def d_front(self):
        return self.front.data

    def d_rear(self):
        return self.rear.data


d = Deque()
d.enqueue_front(1)
d.enqueue_front(2)
d.enqueue_rear(100)
d.enqueue_rear(200)
print(d)
d.delete_front()
d.delete_rear()
print(d)
