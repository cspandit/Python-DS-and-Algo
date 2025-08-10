class X:
    @classmethod
    def class_test(cls):
        print("This is class method")
        cls.age = 0

    def regular_method(self):
        print("This is regular method")
        print(self.age)

if __name__ == '__main__':
    x = X()
    x.class_test()
    x.regular_method()


