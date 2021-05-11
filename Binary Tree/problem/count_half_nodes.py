class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def half_node(temp):
    if temp is None:
        return
    queue = [temp]
    half_count = 0
    while queue:
        node = queue[0]
        queue.pop(0)
        if node.left and not node.right or node.right and not node.left:
            half_count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return half_count


def half_node_recursive(temp, count):
    if temp is None:
        return 0
    if temp.left and not temp.right or temp.right and not temp.left:
        return count + 1
    x = half_node_recursive(temp.left, count)
    y = half_node_recursive(temp.right, count)
    return x+y


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

print(half_node_recursive(root, 0))
