import os.path
import unittest
import my_math
import configparser
from log_config import setup_log

logger = setup_log(__name__)

class TestSub(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(os.getcwd(), 'test_data/test_data.ini'))


    """test class for subtraction test cases"""
    def test_sub_int(self):
        logger.info("Running Test Case:  test_sub_int")
        a = int(self.config.get('integer', 'a'))
        b = int(self.config.get('integer', 'b'))
        res = my_math.subtract(a, b)
        logger.info("Assertion Expected: {} Actual: {}".format(-3, res))
        self.assertEqual(res, -3)


if __name__ == "__main__":
    unittest.main()
