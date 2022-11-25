import unittest
import my_math


class TestSub(unittest.TestCase):
    """test class for subtraction test cases"""
    def test_sub_int(self):
        res = my_math.subtract(5, 2)
        self.assertEqual(res, 3)
        self.assertEqual(res, 4)


if __name__ == "__main__":
    unittest.main()
