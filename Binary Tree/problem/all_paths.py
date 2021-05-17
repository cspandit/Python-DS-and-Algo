# Given a binary tree, prints all its root to leaf paths and also print all sum of all
# nodes in each path


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def all_paths(temp, paths, summ):
    if temp is None:
        return
    paths = paths+str(temp.value) + " "
    summ = summ+temp.value
    if temp.left is None and temp.right is None:
        print(paths)
        print(summ)
    else:
        all_paths(temp.left, paths, summ)
        all_paths(temp.right, paths, summ)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    all_paths(root, "", 0)

