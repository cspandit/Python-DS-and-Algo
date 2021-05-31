class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}

    def add_at_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        if node is not self.tail:
            self.break_links()
            self.add_at_tail()

    def put(self, key, value):
        if key in self.map:
            self.map[key].value = value
            self.get(key)
        if len(self.map) == self.capacity:
            self.map.pop(self.head.key)
            self.remove_head()

        new_node = Node(value)
        self.map[key] = new_node
        self.add_at_tail(new_node)
