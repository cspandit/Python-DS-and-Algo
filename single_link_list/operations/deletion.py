class Node:
    def __init__(self, data):
        self.data = data
        self.Node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\n')

    def delete_position(self, position):
        temp = self.head
        prev = self.head

        for i in range(1, position+1):
            if i == position and position == 1:
                self.head = self.head.next
                temp = None
                prev = None
            elif i == position:
                prev.next = temp.next
                temp = None
            else:
                prev = temp
                temp = temp.next
                # if position is greater than number of element in list
                if temp is None:
                    break

    def deletion_key(self, key):
        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        prev = self.head

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        # if condition is to handle situation if key not present in list
        if temp is not None:
            prev.next = temp.next
            temp = None


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(1, 6):
        ll.insert(i)
    ll.print_list()
    ll.delete_position(6)
    ll.print_list()
    ll.deletion_key(10)
    ll.print_list()

