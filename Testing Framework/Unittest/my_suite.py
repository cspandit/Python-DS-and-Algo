import unittest
from HtmlTestRunner import HTMLTestRunner
from test_my_addmath import TestAdd
from test_my_submath import TestSub


def my_suite():
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestAdd)) --> makeSuite() method is deprecated after --3.11
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSub))
    runner = unittest.TextTestRunner()
    summary = runner.run(suite)
    print(summary)


def my_html_report_runner():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestAdd))
    suite.addTests(loader.loadTestsFromTestCase(TestSub))
    #suite = loader.discover('.', "test_*.py") -> this will not require to add all test file to be added manually
    #in test suite
    runner = HTMLTestRunner(
                            report_name="Sanity_Test_Report",
                            combine_reports=True,
                            output='reports',
                            report_title= 'Sanity Test Report'
                        )
    runner.run(suite)


my_html_report_runner()
#my_suite()
