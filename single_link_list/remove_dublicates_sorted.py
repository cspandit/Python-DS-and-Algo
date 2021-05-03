class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def remove_duplicates_unsorted_stack(self):
        if self.head is None:
            return
        temp_list = []
        temp_prev = None
        temp = self.head
        while temp:
            if temp.data not in temp_list:
                temp_list.append(temp.data)
                temp_prev = temp
                temp = temp.next
            else:
                nex = temp.next
                temp_prev.next = temp.next
                temp = nex

    def remove_duplicates_unsorted_two_loops(self):
        pass

    def remove_duplicates_sorted_iter(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            if temp.data == temp.next.data:
                to_free = temp.next
                temp.next = temp.next.next
                print("freed node ", to_free.data)
            else:
                temp = temp.next

    def remove_duplicates_sorted_recur(self, head):
        if head.next is None:
            return
        if head.data == head.next.data:
            to_free = head.next
            head.next = head.next.next
            print("free node ", to_free.data)
            self.remove_duplicates_sorted_recur(head)
        else:
            self.remove_duplicates_sorted_recur(head.next)


if __name__ == "__main__":
    nodes = [Node(4), Node(4), Node(3), Node(3), Node(2), Node(1), Node(1)]
    linked_list = LinkedList()
    for node in nodes:
        linked_list.push(node)

    linked_list.print_list()
    linked_list.remove_duplicates_unsorted_two_loops()
    linked_list.print_list()
