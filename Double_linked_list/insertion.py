class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self. head = None

    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    @staticmethod
    def insert_after(prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if prev_node.next:
            prev_node.next.prev = new_node

    def insert_before(self, next_node, data):
        new_node = Node(data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        if next_node.prev:
            next_node.prev.next = new_node
            next_node.prev = new_node
        else:
            next_node.prev = new_node
            self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


d_list = DoubleLinkedList()
for i in range(4):
    d_list.insert_start(i)
d_list.print_list()
d_list.insert_before(d_list.head, -100)
d_list.insert_before(d_list.head.next, -200)
d_list.print_list()