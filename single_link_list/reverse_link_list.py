class Node:
    def __init__(self, data):
        self.data =  data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def reverse_list_recur(self, cur, prev):
        if cur and cur.next is None:
            self.head = cur
            cur.next = prev
            return

        n = cur.next
        cur.next = prev

        self.reverse_list_recur(n, cur)

    def reverse_list_iter(self):
        if self.head is None:
            return
        prev = None
        cur = self.head
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        self.head = prev

    def reverse_list_using_stack(self):
        pass

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    node_list = [Node(1), Node(2), Node(3), Node(4)]
    linked_list = LinkedList()

    for new_node in node_list:
        linked_list.push(new_node)

    linked_list.print_list()
    linked_list.reverse_list_recur(linked_list.head, None)
    linked_list.print_list()
