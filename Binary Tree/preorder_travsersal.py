# In pre-order traversal each node is processed before its sub trees.
# Even though each node is processed first, it still required some info to be stored.
# Say a node is processed, then its left node is processed, now to process its right node, info about the node
# is required.
# Stack is must suitable ADS for this situation because of LIFO property.
# Space complexity is O(h) -> h is height of tree


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def preorder(temp):
    if temp is None:
        return
    print(temp.value, end=" ")
    preorder(temp.left)
    preorder(temp.right)


def preorder_recursive(temp):
    if temp is None:
        return
    stack = [temp]
    while len(stack) != 0:
        x = stack.pop()
        print(x.value, end=" ")
        if x.right is not None:
            stack.append(x.right)
        if x.left is not None:
            stack.append(x.left)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    preorder_recursive(root)

