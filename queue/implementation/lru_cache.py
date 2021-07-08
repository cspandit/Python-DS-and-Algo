# Map and doubly linked list queue serve the best. Map is used to acheive search operation in O(1)
# Double linked list makes deletion and insertion operation easy. get() and put() is achieved in O(1)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.search_map = {}

    def __str__(self):
        temp = self.head
        s = "head->"
        while temp:
            s = s + str((temp.key, temp.value)) + "<=>"
            temp = temp.next
        s = s[:-3] + "<- tail"
        return s

    def break_links(self, node):
        if node is self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return

    def add_at_tail(self, new_node):
        if self.tail is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = None

    # there are two conditions: 1. key not present in map(return -1)
    # 2. key is present in map(break links and add search node at tail)
    def get(self, key):
        if key not in self.search_map:
            return -1
        node = self.search_map[key]
        if node is not self.tail:
            self.break_links(node)
            self.add_at_tail(node)
        return node.value

    # There could be three condition: 1. key present in map 2. capacity is full 3. normal put
    def put(self, key, value):
        if key in self.search_map:
            self.search_map[key].value = value
            self.get(key)
            return

        if len(self.search_map) == self.capacity:
            self.search_map.pop(self.head.key)
            self.remove_head()
        new_node = Node(key, value)
        self.search_map[key] = new_node
        self.add_at_tail(new_node)


lru = LRUCache(2)
lru.put(1, 100)
lru.put(2, 200)
print(lru)
print(lru.get(1))
print(lru)
print(lru.put(3, 300))
print(lru)
print(lru.get(4))

