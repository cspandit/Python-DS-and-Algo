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

    def check_palindrome_using_stack(self):
        if self.head is None:
            return
        node_stack = []
        temp = self.head
        while temp:
            node_stack.append(temp.data)
            temp = temp.next

        head = self.head
        while len(node_stack) > 0:
            element = node_stack.pop()
            if element != head.data:
                return False
            head = head.next

        if head is None and len(node_stack) == 0:
            return True
        return False

    def check_palindrome(self):
        slow = self.head
        fast = self.head

        mid_node = None
        slow_prev = None
        result = False

        while slow and fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            mid_node = slow
            slow = slow.next

        slow_prev.next = None
        slow = self.reverse(slow)
        result = self.comparision(self.head, slow)
        slow = self.reverse(slow)

        if mid_node is not None:
            slow_prev.next = mid_node
            mid_node.next = slow
        else:
            slow_prev.next = slow
        return result

    @staticmethod
    def reverse(head):
        cur = head
        prev = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        head = prev
        return head

    @staticmethod
    def comparision(head1, head2):
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            return True
        return False

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    nodes = [Node(1), Node(1), Node(1), Node(2)]
    linked_list1 = LinkedList()
    linked_list12 = LinkedList()

    for node in nodes:
        linked_list1.push(node)
        # linked_list12.push(node)

    # linked_list1.print_list()
    # linked_list12.print_list()

    # linked_list12.push(Node(100))
    linked_list1.print_list()
    # print(linked_list1.comparision(linked_list1.head, linked_list12.head))
    print(linked_list1.check_palindrome_using_stack())
    linked_list1.print_list()
