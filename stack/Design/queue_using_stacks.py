# Queue can be implemented using two stacks with push() and pop() operations
# Time complexity of enqueue operation is O(n) and dequeue is O(1)
# Queue can be even implemented making dequeue operation costly.


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(data)

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):
        if len(self.stack1) == 0:
            print("Underflow")
        else:
            return self.stack1.pop()

    # def dequeue_costly(self):
    #     if len(self.stack1) == 0 and len(self.stack2) == 0:
    #         return
    #     elif len(self.stack1) > 0 and len(self.stack2) == 0:
    #         while len(self.stack1) > 0:
    #             self.stack2.append(self.stack1.pop())
    #         return self.stack2.pop()
    #     else:
    #         return self.stack2.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.stack1)
print(q.dequeue())
print(q.stack1)