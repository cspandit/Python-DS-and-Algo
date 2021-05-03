import unittest
from Test_lib.factorial_recur import fact


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertAlmostEqual(fact(5), 5*4*3*2*1)

