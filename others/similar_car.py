class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            return
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

def solution(cars):
    llist = CircularLinkedList()
    for x in cars:
        llist.push(x)

    temp_head = llist.head
    temp = temp_head.next
    similar_count = 0
    output = []
    while True:
        if temp is not temp_head:
            if is_similar(temp_head.data, temp.data):
                similar_count += 1
            temp = temp.next
        else:
            output.append(similar_count)
            similar_count = 0
            temp_head = temp_head.next
            if temp_head is llist.head:
                break
            temp = temp_head.next

    return output


def is_similar(a, b):
    diff_count = sum(c1 != c2 for c1, c2 in zip(a, b))
    if diff_count > 1:
        return False
    else:
        return True


cars = ['0011', '0111', '0111', '0110', '0000']
print(solution(cars))