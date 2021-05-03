class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_empty(self, data):
        if self.last is not None:
            return
        new_node = Node(data)
        self.last = new_node
        self.last.next = new_node

    def insert_beginning(self, data):
        if self.last is None:
            self.insert_empty(data)
            return
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node

    def insert_end(self, data):
        if self.last is None:
            self.insert_empty(data)
            return
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def insert_after(self, data, key):
        if self.last is None:
            return
        temp = self.last.next
        while True:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next
            if temp is self.last.next:
                break

    def print_list(self):
        if self.last is None:
            return
        temp = self.last.next
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp is self.last.next:
                break
        print("\n")


if __name__ == "__main__":
    llist = CircularLinkedList()
    llist.insert_empty(3)
    llist.insert_beginning(2)
    llist.insert_beginning(1)

    llist.print_list()

    llist.insert_end(4)
    llist.print_list()

    llist.insert_after(100, 2)
    llist.print_list()
