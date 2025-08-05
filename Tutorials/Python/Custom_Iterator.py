class MyIterator:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.counter = 0
        self.max = len(self.iterable_object)-1

    def __iter__(self):
        self

    def __next__(self):
        while self.counter <= self.max:
            self.counter += 1
            return self.iterable_object[self.counter-1]
        if self.counter > self.max:

            raise StopIteration


x = 'chandra'
y = MyIterator(x)
print(y.__next__())
print(next(y))
