import unittest
import BeautifulReport

test_suite =unittest.TestSuite()

all_case =unittest.defaultTestLoader.discover('cases','*.py')
[test_suite.addTest(case) for case in all_case]
report = br.BeautifulReport(test_suite)
return report(description ='报告描述',filename ='文件名称1.html')
