class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            last = self.head
            while last.next is not self.head:
                last = last.next
            last.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node

    def delete(self, key):
        # if list is empty
        if self.head is None:
            return

        # if head is to be delete
        if self.head.data == key:
            last = self.head
            while last.next is not self.head:
                last = last.next
            last.next = self.head.next
            self.head = last.next
            return

        last = self.head
        d = None
        while last.next and last.next.data != key:
            last = last.next
        d = last.next
        last.next = d.next

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while True:
            print(temp.data, end =" ")
            temp = temp.next
            if temp is self.head:
                break
        print("\n")


if __name__ == "__main__":
    llist = CircularLinkedList()
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(0)

    llist.print_list()

    llist.delete(3)
    llist.print_list()