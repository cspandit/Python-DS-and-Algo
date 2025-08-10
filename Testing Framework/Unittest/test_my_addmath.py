import my_math
import unittest
import configparser
import os
import sys
import json
from log_config import setup_log

logger = setup_log(__name__)


class TestAdd(unittest.TestCase):
	"""Let's just create a test suite for add function in my_math. Any class variable can
	be accessed all objects of the class. Within instacne method variable it can be accessed using
	'self'
	"""

	@classmethod
	def setUp(cls):
		"""To create config from a input  file"""
		logger.info("Loading test data from the test data json file")
		file_path = os.path.join(os.getcwd(), 'test_data/test_data.json')
		cls.test_data_file = open(file_path, 'r')
		cls.test_data = json.load(cls.test_data_file)

	def test_add_int(self):
		logger.info("Running Test Case:  test_add_int")
		a = self.test_data['test_data']['integer']['a']
		b = self.test_data['test_data']['integer']['b']
		res = my_math.add(a, b)
		logger.info("Assertion Expected: {} Actual: {}".format(100, res))
		self.assertEqual(res, 100)

	@unittest.skip("Skip this test case")
	def test_add_float(self):
		logger.info("Running Test Case:  test_add_float")
		a = self.test_data['test_data']['float']['a']
		b = self.test_data['test_data']['float']['b']
		res = my_math.subtract(a, b)
		logger.info("Assertion Expected: {} Actual: {}".format(5.8, res))
		self.assertEqual(res, 5.8)

	@unittest.skipIf(sys.platform == 'win32', 'does not requires to run on windows')
	def test_add_string(self):
		logger.info("Running Test Case:  test_add_string")
		a = self.test_data['test_data']['string']['a']
		b = self.test_data['test_data']['string']['b']
		res = my_math.add(a, b)
		logger.info("Assertion Expected: {} Actual: {}".format('Chandra Pandit', res))
		self.assertEqual(res, 'Chandra Pandit')

	def tearDown(self):
		"""This like closing file or database connection or delete db
		can be included under tearDown"""
		self.test_data_file.close()
		logger.info("closing the test data file")


if __name__ == "__main__":
	unittest.main()
