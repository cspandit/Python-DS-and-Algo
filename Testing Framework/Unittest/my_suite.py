import unittest
from Unittest.test_my_addmath import TestAdd
from Unittest.test_my_submath import TestSub

def my_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSub))
    runner = unittest.TextTestRunner()
    summary = runner.run(suite)
    print(summary)


my_suite()
