class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self. head = None

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

    def reverse(self):
        if self.head is None:
            return
        pre = None
        cur = self.head
        while cur:
            nex = cur.next
            cur.next = pre
            cur.pre = nex
            pre = cur
            cur = nex
        self.head = pre

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


d_list = DoubleLinkedList()
for i in range(4):
    d_list.insert_end(i)
d_list.print_list()
d_list.reverse()
d_list.print_list()