import unittest
from Test_lib.fibonacci_recur import fib


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(10), 55, "10th fibonacci number is 55")


