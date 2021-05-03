class Node:
    def __init__(self):
        self.data = 0
        self.next = None


def push(head, data):
    new_node = Node()
    new_node.data = data

    new_node.next = (head)
    (head) = new_node
    return head


def intersection(l1, l2):
    dummy = Node()
    tail = dummy
    dummy.next = None

    while l1 and l2:
        if l1.data == l2.data:
            tail.next = push((tail.next), l1.data)
            l1 = l1.next
            l2 = l2.next

        elif l1.data < l2.data:
            l1 = l1.next
        else:
            l2 = l2.next

    return tail.next


def print_list(head):
    if head is None:
        return

    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print("\n")


if __name__ == "__main__":
    a = None
    b = None
    list1 = [6, 5, 4, 3, 2, 1]
    list2 = [8, 6, 4, 2]

    for data in list1:
        a = push(a, data)

    for data in list2:
        b = push(b, data)

    print_list(a)
    print_list(b)

    inter_head = intersection(a, b)
    print_list(inter_head)
