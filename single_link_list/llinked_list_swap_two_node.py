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

    def swap(self, key1, key2):
        if self.head is None:
            return
        curX = self.head
        curY = self.head
        prevX = None
        prevY = None

        while curX is not None and curX.data != key1:
            prevX = curX
            curX = curX.next

        while curY is not None and curY.data != key2:
            prevY = curY
            curY = curY.next

        # if one or both keys are not present in list
        if curX is None or curY is None:
            return

        if prevX is not None:
            prevX.next = curY
        # if curX is head
        else:
            self.head = curY

        if prevY is not None:
            prevY.next = curX
        # if curY is head
        else:
            self.head = curX

        temp = curX.next
        curX.next = curY.next
        curY.next = temp

    def swap_pair(self):
        if self.head is None:
            return
        cur = self.head

        if cur.data == cur.next.data:
            cur = cur.next.next

        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next

    def print_list(self):
        if self.head is None:
            return
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)]
    linked_list = LinkedList()
    for node in nodes:
        linked_list.append(node)

    linked_list.print_list()
    linked_list.swap_pair()
    linked_list.print_list()