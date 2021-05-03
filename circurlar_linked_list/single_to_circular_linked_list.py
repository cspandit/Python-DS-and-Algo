class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_single(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_circular(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            last = self.head
            while last.next is not self.head:
                last = last.next

            last.next = new_node

        else:
            new_node.next = new_node
        self.head = new_node

    def single_to_circular(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head

    def print_list(self):
        if self.head is None:
            return
        temp = self.head.next
        print(self.head.data, end=" ")
        while temp is not None and temp is not self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def print_single(self):
        if self.head is None:
            return
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    single_list = LinkedList()
    circular_list = LinkedList()

    single_list.push_single(3)
    single_list.push_single(2)
    single_list.push_single(1)

    single_list.print_list()

    circular_list.push_circular(9)
    circular_list.push_circular(8)
    circular_list.push_circular(7)
    circular_list.push_circular(6)

    circular_list.print_list()
    single_list.single_to_circular()
    single_list.print_single()
