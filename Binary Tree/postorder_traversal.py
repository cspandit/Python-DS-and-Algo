# In post-order traversal each node is visited twice. Once after left node is processed
# and next after right node is processed.
# Idea is to mark the node visited after its right node is processed.
# Store each node in stack and pop out condition can be two:
# 1. if prev node is parent node and the node has no children
# 2. if the not is already visited


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def postorder(temp):
    if temp is None:
        return
    postorder(temp.left)
    postorder(temp.right)
    print(temp.value, end=" ")


def postorder_recursive(temp):
    if temp is None:
        return
    stack = []
    node = temp
    visited = set()
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            x = stack.pop()
            if x.right and x.right not in visited:
                visited.add(x)
                # parent node is required after right node is processed
                stack.append(x)
                node = x.right
            else:
                visited.add(x)
                print(x.value, end=" ")
                node = None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    postorder_recursive(root)
