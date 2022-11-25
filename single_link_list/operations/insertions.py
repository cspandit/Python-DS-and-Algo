class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = Node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    @staticmethod
    def insert_after(prev_node, data):
        node = Node(data)
        if prev_node is None:
            return
        node.next = prev_node.next
        prev_node.next = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print('\r')


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(1)
    ll.push(4)
    ll.push(6)
    ll.push(10)
    ll.print_list()
    ll.insert_at_end(100)
    ll.print_list()
    x = ll.head
    while x.data != 6:
        x = x.next
    ll.insert_after(x, 200)
    ll.print_list()