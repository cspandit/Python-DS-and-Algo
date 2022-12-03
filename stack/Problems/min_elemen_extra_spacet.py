# get min element in stack in O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        if len(self.stack) == 0:
            self.stack.append(item)
            self.min_stack.append(item)
        else:
            if self.stack[-1] <= item:
                self.stack.append(item)
            else:
                self.stack.append(item)
                self.min_stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            if self.stack[-1] != self.min_stack[-1]:
                return self.stack.pop()
            else:
                self.min_stack.pop()
                return self.stack.pop()
    def get_min(self):
        return self.min_stack[-1]

if __name__ == '__main__':
    ss = MinStack()
    ss.push(5)
    ss.push(3)
    ss.push(7)
    print(ss.get_min())
    ss.push(1)
    print(ss.get_min())
    ss.pop()
    print(ss.get_min())