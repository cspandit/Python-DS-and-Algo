import my_math
import unittest
import configparser
import os
import sys
import json


class TestAdd(unittest.TestCase):
	"""Let's just create a test suite for add function in my_math. Any class variable can
	be accessed all objects of the class. Within instacne method variable it can be accessed using
	'self'
	"""

	@classmethod
	def setUp(cls):
		"""To create config from a input  file"""
		file_path = os.path.join(os.getcwd(), 'test_data.json')
		cls.test_data_file = open(file_path, 'r')
		cls.test_data = json.load(cls.test_data_file)

	def test_add_int(self):
		a = self.test_data['test_data']['integer']['a']
		b = self.test_data['test_data']['integer']['b']
		res = my_math.add(a, b)
		self.assertEqual(res, 6)

	@unittest.skip("Skip this test case")
	def test_add_float(self):
		a = self.test_data['test_data']['float']['a']
		b = self.test_data['test_data']['float']['b']
		res = my_math.subtract(a, b)
		self.assertEqual(res, 5.8)

	@unittest.skipIf(sys.platform == 'win32', 'does not requires to run on windows')
	def test_add_string(self):
		a = self.test_data['test_data']['string']['a']
		b = self.test_data['test_data']['string']['b']
		res = my_math.add(a, b)
		self.assertEqual(res, 'Chandra Pandit')

	def tearDown(self):
		"""This like closing file or database connection or delete db
		can be included under tearDown"""
		self.test_data_file.close()



if __name__ == "__main__":
	unittest.main()
