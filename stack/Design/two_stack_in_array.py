# problem is to two stack in an array and it should be space efficient


class TwoStack:
    def __init__(self, array):
        self.array = array
        self.top1 = -1
        self.top2 = len(self.array)

    def push1(self, value):
        if self.top1 + 1 < self.top2:
            self.array[self.top1+1] = value
            self.top1 += 1
        else:
            raise Exception("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:
            remove = self.array[self.top1]
            self.array[self.top1] = 0
            self.top1 -= 1
            return remove
        else:
            raise Exception("Stack Underflow")

    def push2(self, value):
        if self.top1+1 < self.top2:
            self.array[self.top2-1] = value
            self.top2 -= 1
        else:
            raise Exception("Stack Overflow")

    def pop2(self):
        if self.top2 < len(self.array):
            remove = self.array[self.top2]
            self.array[self.top2] = 0
            self.top2 += 1
            return remove
        else:
            raise Exception("Stack Underflow")


if __name__ == "__main__":
    a = [0]*5
    stacks = TwoStack(a)
    stacks.push1(1)
    stacks.push1(2)
    print(a)
    stacks.push2("A")
    stacks.push2("B")
    print(a)

    # print(stacks.pop1())
    # print(stacks.pop2())
    # stacks.push2("C")
    # stacks.push1(3)

    print(a)
