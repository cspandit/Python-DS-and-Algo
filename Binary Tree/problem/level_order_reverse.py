class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def level_order_reverse(temp):
    if temp is None:
        return
    queue = [temp]
    stack = []
    while queue:
        x = queue[0]
        queue.pop(0)
        if x.right:
            queue.append(x.right)
        if x.left:
            queue.append(x.left)
        stack.append(x)

    while stack:
        x = stack.pop()
        print(x.value, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

level_order_reverse(root)