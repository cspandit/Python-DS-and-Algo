class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def quick_sort(self, start, end):
        if start is None or end is None:
            return
        pivot_prev = self.partition(start, end)
        self.quick_sort(start, pivot_prev)

        if pivot_prev is not None and pivot_prev is start:
            self.quick_sort(pivot_prev.next, end)
        elif pivot_prev is not None and pivot_prev is not start:
            self.quick_sort(pivot_prev.next.next, end)

    @staticmethod
    def partition(start, end):
        if start is None or end is None or start is end:
            return
        pivot_prev = start
        pivot_position = start
        pivot = end.data

        while start is not end:
            if start.data < pivot:
                pivot_prev = pivot_position
                temp = pivot_position.data
                pivot_position.data = start.data
                start.data = temp
                pivot_position = pivot_position.next
            start = start.next

        temp = pivot_position.data
        pivot_position.data = pivot
        end.data = temp

        return pivot_prev

    def print_list(self):
        if self.head is None:
            return
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    nodes1 = [Node(30), Node(3), Node(4), Node(20), Node(5)]

    linked_list1 = LinkedList()
    for node in nodes1:
        linked_list1.append(node)

    linked_list1.print_list()
    start = linked_list1.head
    end = linked_list1.head
    while end.next:
        end = end.next
    linked_list1.quick_sort(start, end)
    linked_list1.print_list()



