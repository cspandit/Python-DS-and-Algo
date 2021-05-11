class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def compare(temp1, temp2):
    if temp1 is None and temp2 is None:
        return True
    if temp1 and temp2:
        left_compare_result = compare(temp1.left, temp2.left)
        right_compare_result = compare(temp2.left, temp2.right)
        return left_compare_result and right_compare_result

    return False


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.left = Node(6)
    root1.right.right = Node(7)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.right.left = Node(6)
    root2.right.right = Node(7)
    # root2.left.left.left = Node(100)


print(compare(root1, root2))
