class MinStack:
    def __init__(self):
        self.stack = []
        self.min_element = -1

    def push(self, item):
        if len(self.stack) == 0:
            self.stack.append(item)
            self.min_element = item
        else:
            if self.stack[-1] <= item:
                self.stack.append(item)
            else:
                flag = 2*item-self.min_element
                self.stack.append(flag)
                self.min_element = item

    def pop(self):
        if len(self.stack) == 0:
            return
        else:
            if self.stack[-1] >= self.min_element:
                self.stack.pop()
            else:
                self.min_element = 2*self.min_element-self.stack[-1]
                self.stack.pop()



if __name__ == '__main__':
    ss = MinStack()
    ss.push(5)
    ss.push(3)
    print(ss.min_element)
    ss.push(7)
    print(ss.min_element)
    ss.push(1)
    print(ss.min_element)
    ss.pop()
    print(ss.min_element)
    ss.pop()
    print(ss.min_element)

