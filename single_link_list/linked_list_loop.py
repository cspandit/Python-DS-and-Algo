class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = 0


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node.next = self.head
        self. head = new_node

    def create_loop(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = self.head

    def detect_loop_floyd_cycle(self):
        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def detect_loop_hash_map(self):
        if self.head is None:
            return False
        mapp = set()
        temp = self.head
        while temp:
            if temp in mapp:
                return True
            mapp.add(temp)
            temp = temp.next
        return False

    def detect_loop_extra_flag(self):
        if self.head is None:
            return False
        temp = self.head
        while temp:
            if temp.flag == 1:
                return True
            temp.flag = 1
            temp = temp.next
        return False

    def detect_loop_pointer(self):
        if self.head is None:
            return False

        temp = self.head
        while temp:
            if temp.next == "":
                return True
            nex = temp.next
            temp.next = ""
            temp = nex

        return False

    def loop_length(self):
        if self.head is None:
            return 0

        slow = self.head
        fast = self.head
        count = 1
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = slow.next
                while slow != fast:
                    count += 1
                    slow = slow.next
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
    linked_list = LinkedList()
    nodes = [Node(5), Node(4), Node(3), Node(2), Node(1)]

    for node in nodes:
        linked_list.push(node)

    linked_list.print_list()
    node = Node(100)
    linked_list.push(node)
    linked_list.create_loop()
    print(linked_list.detect_loop_floyd_cycle())
    print(linked_list.loop_length())



