# Priority Queues can be implemented using common data structures like arrays, linked-lists, heaps and binary trees.
# Priority Queues using linked list -> Push() is O(n), Pop() is O(1) and Peek() is O(1)
# Priority Queues using Binary heap -> Push() is O(nlogn), Pop() is O(nlogn) and Peek is O(1)


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def __str__(self):
        temp = self.front
        s = ""
        while temp:
            s = s + str(temp.data) + "->"
            temp = temp.next
        return s[:-2]

    def push(self, data, priority):
        new_node = Node(data, priority)
        if self.front is None:
            self.front = new_node
            return
        if self.front.priority < priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next is not None and temp.next.priority < priority:
                temp = temp.next
            if temp.next is None:
                temp.next = new_node
            else:
                new_node.next = temp.next
                temp.next = new_node

    def pop(self):
        temp = self.front
        self.front = temp.next
        return temp.data

    def peek(self):
        return self.front.data


pq = PriorityQueue()
pq.push(100, 4)
pq.push(200, 3)
pq.push(300, 1)
pq.push(400, 2)

print(pq)
print(pq.pop())
print(pq)
