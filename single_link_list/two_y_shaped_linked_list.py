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

    @staticmethod
    def find_intersection(cur1, cur2, d):
        while d:
            cur1 = cur1.next
            d -= 1

        while cur1 and cur2:
            if cur1.data == cur2.data:
                return cur1.data
            cur1 = cur1.next
            cur2 = cur2.next
        return None

    def intersection_driver(self, head1, head2):
        if head1 is None or head2 is None:
            return
        a = self.get_count(head1)
        b = self.get_count(head2)
        x = None
        if a > b:
            x = self.find_intersection(head1, head2, a-b)
        else:
            x = self.find_intersection(head2, head1, b-a)

        return x

    @staticmethod
    def get_count(temp):
        if temp is None:
            return 0
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        if self.head is None:
            return
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    nodes1 = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(12), Node(13)]
    nodes2 = [Node(10), Node(11), Node(13)]

    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    for node in nodes1:
        linked_list1.append(node)
    for node in nodes2:
        linked_list2.append(node)

    linked_list1.print_list()
    linked_list2.print_list()
    print(linked_list1.intersection_driver(linked_list1.head, linked_list2.head))

