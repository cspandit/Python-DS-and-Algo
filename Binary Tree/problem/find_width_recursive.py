class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_height(temp):
    if temp is None:
        return 0
    left_height = find_height(temp.left)
    right_height = find_height(temp.right)
    return left_height+right_height+1


def find_width(temp, level):
    if temp is None:
        return 0
    if level == 1:
        return 1
    left_width = find_width(temp.left, level-1)
    right_width = find_width(temp.right, level-1)
    return left_width + right_width


def find_max_width(temp):
    if temp is None:
        return 0
    height = find_height(temp)
    max_width = -1
    for i in range(1, height+1):
        width = find_width(temp, i)
        max_width = max(max_width, width)
    return max_width


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(find_max_width(root))
