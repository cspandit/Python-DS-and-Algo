# Problem : https://www.geeksforgeeks.org/the-celebrity-problem/


class Celebrity:
    def __init__(self, matrix):
        self.matrix = matrix
        self.stack = []

    def knows(self, a, b):
        return self.matrix[a][b]

    def find_celebrity(self, n):
        for i in range(n):
            self.stack.append(i)

        while len(self.stack) > 1:
            a = self.stack.pop()
            b = self.stack.pop()

            if self.knows(a, b):
                self.stack.append(b)
            else:
                self.stack.append(a)

        c = self.stack[-1]

        for i in range(n):
            if i != c and self.knows(c, i):
                return None
        return c


A = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
n = len(A)
C = Celebrity(A)
print(C.find_celebrity(n))
