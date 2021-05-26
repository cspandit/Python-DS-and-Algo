from Unittest import my_math
import unittest
import configparser
import os
import sys


class TestAdd(unittest.TestCase):
	"""Lets just create a test suite for add function in my_math"""
	def setUp(self):
		"""To create config from a input  file"""
		self.config = configparser.ConfigParser()
		self.config.read(os.path.join(os.getcwd(), 'test_data.ini'))

	def test_add_int(self):
		a = int(self.config.get('integer', 'a'))
		b = int(self.config.get('integer', 'b'))
		res = my_math.add(a, b)
		self.assertEqual(res, 7)

	@unittest.skip("Skip this test case")
	def test_add_float(self):
		res = my_math.add(2.1, 7.9)
		self.assertEqual(res, 10.0)

	@unittest.skipIf(sys.platform == 'win32', 'does not requires to run on windows')
	def test_add_string(self):
		a = self.config.get('string', 'a')
		b = self.config.get('string', 'b')
		res = my_math.add(a, b)
		self.assertEqual(res, 'chandra_pandit')

	def tearDown(self):
		"""This like closing file or data base connection or delete db
		can be included under tearDown"""
		pass


if __name__ == "__main__":
	unittest.main()
