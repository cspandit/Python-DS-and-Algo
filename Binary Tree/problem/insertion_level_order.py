# The idea is to do iterative level order traversal of the given tree using queue.
# If we find a node whose left child is empty, we make new key as left child of the node.


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


def insert_level_order(temp, key):
    if not temp:
        root = Node(key)
        return
    queue = [temp]
    while len(queue) != 0:
        x = queue[0]
        queue.pop(0)
        if not x.left:
            x.left = Node(key)
            break
        else:
            queue.append(x.left)
        if not x.right:
            x.right = Node(key)
            break
        else:
            queue.append(x.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    inorder(root)
    print("\n")
    insert_level_order(root, 12)
    inorder(root)

