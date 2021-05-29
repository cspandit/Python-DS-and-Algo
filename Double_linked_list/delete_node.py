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

    def delete_node(self, del_node):
        nex = del_node.next
        pre = del_node.prev

        if nex is None and pre is None:
            self.head = None
            return
        elif pre is None:
            nex.prev = None
            self.head = nex
        elif nex is None:
            pre.next = None
        else:
            nex.prev = pre
            pre.next = nex

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

d_list.delete_node(d_list.head.next)
d_list.print_list()