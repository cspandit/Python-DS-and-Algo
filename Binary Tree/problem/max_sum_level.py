# Given a tree find a level which has max sum
# Space complexity O(n) and time complexity O(n)


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Time complexity O(n2) and space complexity O(w) w->width
def max_sum_level_1(temp):
    if temp is None:
        return
    queue = [temp]
    max_level = 0
    cur_level = 0
    max_sum = 0
    cur_sum = 0
    while True:
        width = len(queue)
        cur_level += 1
        if width == 0:
            return max_level
        cur_sum = 0
        while width > 0:
            node = queue[0]
            queue.pop(0)
            cur_sum = cur_sum + node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            width -= 1

        if cur_sum > max_sum:
            max_sum = cur_sum
            max_level = cur_level


# Time complexity O(n2) and space complexity O(w+1) w->width
def max_sum_level_2(temp):
    if temp is None:
        return 0
    queue = [temp, None]
    max_sum = 0
    cur_sum = 0
    cur_level = 1
    max_level = 1
    while queue:
        node = queue[0]
        queue.pop(0)
        if node is None:
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = cur_level
            cur_sum = 0
            if queue:
                cur_level += 1
                queue.append(node)
        else:
            cur_sum += node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max_level


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(300)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(700)

    print(max_sum_level_2(root))
