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
    return max(left_height, right_height) + 1


# time complexity O(h*w) -> h is max height, w i max width
def find_height_iterative(temp):
    if temp is None:
        return 0
    stack = [temp]
    depth = 0
    while True:
        len_count = len(stack)
        if len_count == 0:
            return depth
        depth += 1
        while len_count > 0:
            node = stack[0]
            stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            len_count -= 1


# Time complexity  is O(h) - max height of tree
def find_height_iterative_second(temp):
    if temp is None:
        return
    q = [(temp, 1)]
    height = 0
    while q:
        x = q[0]
        q.pop(0)
        node, temp_height = x
        height = max(height, temp_height)
        if node.left:
            q.append((node.left, height+1))
        if node.right:
            q.append((node.right, height+1))
    return height


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(find_height_iterative_second(root))
