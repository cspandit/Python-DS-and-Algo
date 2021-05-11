class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_width(temp):
    if temp is None:
        return
    queue = [temp]
    max_width = -1
    while True:
        width = len(queue)
        if width == 0:
            return max_width
        else:
            max_width = max(max_width, width)
        while width > 0:
            node = queue[0]
            queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            width -= 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(find_width(root))