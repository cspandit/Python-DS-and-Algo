class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def count_node_iter(self, key):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == key:
                self.count += 1
            temp = temp.next
        return self.count

    def count_node_recur(self, temp, key):
        if temp is None:
            return self.count

        if temp.data == key:
            self.count += 1

        return self.count_node_recur(temp.next, key)

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    linked_list = LinkedList()
    nodes = [Node(1), Node(1), Node(2), Node(3), Node(1), Node(2), Node(4)]

    for node in nodes:
        linked_list.append(node)

    linked_list.print_list()
    print(linked_list.count_node_recur(linked_list.head, 3))



