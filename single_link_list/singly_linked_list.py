class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        item.next = self.head
        self.head = item

    def append(self, item):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = item

    def insert_after_node(self, prev_node, new_node):
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after_position(self, position,  new_node):
        if self.head is None:
            return
        if position == 0:
            self.push(new_node)
            return
        prev = self.head
        for i in range(position-1):
            prev = prev.next
            if prev is None:
                break

        if prev is None:
            return
        elif prev.next is None:
            prev.next = new_node
        else:
            new_node.next = prev.next
            prev.next = new_node

    def delete_list(self):
        current = self.head
        while current:
            temp = current.next
            del current.data
            current = temp

    def delete_after_position(self, position):
        if self.head is None:
            return

        prev = self.head
        for i in range(position-1):
            if prev is None:
                break
            prev = prev.next

        if prev is None:
            return
        if prev.next is None:
            return
        else:
            temp = prev.next.next
            prev.next = None
            prev.next = temp

    def delete_node(self, key):
        if self.head is None:
            return
        temp = self.head
        if key == temp.data:
            self.head = temp.next
            temp = None

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return
        else:
            prev.next = temp.next
            temp = None

    def search_iter(self, key):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def search_recur(self, temp_list, key):
        if temp_list is None:
            return False
        if temp_list.data == key:
            print("Found")
            return True
        return self.search_recur(temp_list.next, key)

    def find_nth_node(self, n):
        if self.head is None:
            return
        count = 1
        temp = self.head
        while temp:
            if count == n:
                break
            temp = temp.next
            count += 1
        if temp is None:
            return
        else:
            return temp.data

    def find_nth_node_from_end(self, n):
        if self.head is None:
            return
        length = self.list_length_iter()
        if n > length:
            print("{} is greater than lenght of the list: {}".format(n, length))

        temp = self.head
        for i in range(length-n):
            temp = temp.next

        return temp.data

    def list_length_iter(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length

    def list_length_recur(self, temp):
        if temp is None:
            return 0
        return 1 + self.list_length_recur(temp.next)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(5, 0, -1):
        node = Node(i)
        linked_list.push(node)

    # node = Node(5)
    # linked_list.append(node)
    # node = Node(100)
    # linked_list.insert_after_node(linked_list.head.next, node)
    # node = Node(200)
    # linked_list.insert_after_position(2, node)
    # linked_list.print_list()
    # linked_list.delete_after_position(3)
    # linked_list.delete_node(linked_list.head.next.next)
    # linked_list.delete_node(1)
    linked_list.print_list()
    print(linked_list.find_nth_node_from_end(5))
    # print(linked_list.find_nth_node(3))
    # print(linked_list.search_recur(linked_list.head, 5))
    print(linked_list.list_length_iter())


