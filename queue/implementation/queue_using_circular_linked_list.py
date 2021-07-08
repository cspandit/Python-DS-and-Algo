class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        if self.front is None:
            self.front = new_node
            return
        if self.front.priority < priority:
            new_node.next = self.front
            self.front = new_node
        temp = self.front
        while temp.next is not None and temp.next.priority > priority:
            temp = temp.next
        if temp.next is None:
            temp.next = new_node
        else:
            new_node.next = temp.next
            temp.next = new_node




q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q)