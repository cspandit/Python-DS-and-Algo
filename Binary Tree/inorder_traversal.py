class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.value, end=" ")
    inorder(temp.right)


def inorder_recursive(temp):
    if temp is None:
        return
    stack = []
    node = temp
    result = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            x = stack.pop()
            result.append(x.value)
            node = x.right
    print(result)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    inorder_recursive(root)
