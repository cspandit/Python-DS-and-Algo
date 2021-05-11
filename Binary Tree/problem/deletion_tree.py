# 1. Do level order traversal to find the element to be deleted
# 2. Replace to be deleted node with deepest right most node
# 3. Delete deepest right most node

# This is different from BST deletion


class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.value, end=" ")
    inorder(temp.right)


def delete_deepest(temp, d_node):
    queue = [temp]
    while len(queue) != 0:
        x = queue[0]
        queue.pop(0)
        if x.right is not None:
            if x.right is d_node:
                x.right = None
                return
            else:
                queue.append(temp.right)
        if x.left is not None:
            if x.left is d_node:
                x.left = None
            else:
                queue.append(temp.left)


def deletion(root, key):
    if root is None:
        return
    if root.left is None and root.right is None:
        if root.value == key:
            return None
        else:
            return root

    queue = [root]
    key_node = None
    temp = None
    while len(queue) != 0:
        temp = queue[0]
        queue.pop(0)
        if temp.value == key:
            key_node = temp
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
    if key_node:
        x = temp.value
        delete_deepest(root, temp)
        key_node.value = temp.value
    return root


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    inorder(root)
    print("\n")
    root = deletion(root, 12)
    inorder(root)
