import os.path
import unittest
import my_math
import configparser

class TestSub(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.getcwd(), 'test_data.ini'))


    """test class for subtraction test cases"""
    def test_sub_int(self):
        a = int(self.config.get('integer', 'a'))
        b = int(self.config.get('integer', 'b'))
        res = my_math.subtract(a, b)
        self.assertEqual(res, -3)


if __name__ == "__main__":
    unittest.main()
