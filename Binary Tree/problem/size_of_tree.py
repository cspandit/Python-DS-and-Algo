# size if total numbers of node in a tree


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_size(temp):
    if temp is None:
        return 0
    left_sum = find_size(temp.left)
    right_sum = find_size(temp.right)
    return left_sum + right_sum + 1
    # return find_size(temp.left) + find_size(temp.right) + 1


def find_size_iterative(temp):
    if temp is None:
        return 0
    size = 0
    stack = [temp]
    while stack:
        x = stack.pop()
        size += 1
        if x.left:
            stack.append(x.left)
        if x.right:
            stack.append(x.right)
    return size


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(20)
    root.right = Node(10)
    root.left.left = Node(40)
    root.left.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(7)

print(find_size_iterative(root))
