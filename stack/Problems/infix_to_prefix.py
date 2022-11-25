class Conversion:
    def __init__(self):
        self.stack = []
        self.output = []
        self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    @staticmethod
    def is_operand(ch):
        return ch.isalpha()

    def not_greater(self, op):
        try:
            if op == "^" and self.stack[-1] == "^":
                return True
            else:
                a = self.precedence[op]
                b = self.precedence[self.stack[-1]]
                return True if b > a else False
        except KeyError:
            return False

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def convert(self, exp):
        n = len(exp)
        for i in range(n-1, -1, -1):
            ch = exp[i]
            if self.is_operand(ch):
                self.output.append(ch)

            elif ch == ")":
                self.stack.append("(")

            elif ch == "(":
                while len(self.stack) > 0 and self.stack[-1] != "(":
                    self.output.append(self.stack.pop())

                if len(self.stack) == 0:
                    return -1
                else:
                    self.stack.pop()
            else:
                while not self.is_empty() and self.not_greater(ch):
                    self.output.append(self.stack.pop())
                self.stack.append(ch)

        while len(self.stack) > 0:
            self.output.append(self.stack.pop())

        self.output.reverse()
        print("".join(self.output))


if __name__ == "__main__":
    exp = "x+y*z/(w+u)"
    obj = Conversion()
    obj.convert(exp)
