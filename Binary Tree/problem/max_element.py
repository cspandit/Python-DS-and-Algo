# Traverse each node and compare max

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


def find_max(temp, max_value):
    if temp is None:
        return max_value

    max_value = max(max_value, temp.value)
    max_value = find_max(temp.left, max_value)
    max_value = find_max(temp.right, max_value)
    return max_value


def find_max_iterative(temp):
    if temp is None:
        return
    stack = [temp]
    max_value = -1
    while len(stack) != 0:
        x = stack.pop()
        max_value = max(x.value, max_value)
        if x.right is not None:
            stack.append(x.right)
        if x.left is not None:
            stack.append(x.left)
    return max_value


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(20)
    root.right = Node(10)
    root.left.left = Node(40)
    root.left.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(7)

    print(find_max_iterative(root))

