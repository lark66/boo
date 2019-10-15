import ddt

import unittest

@ddt.ddt

class TestCase(unittest.TestCase):
    def setUp(self):
        print("Before every test case!")\
    @ddt.file_data('testdata_dic.json')

    def test_case_01(self,start,end,value):

        print("start is: " + str(start))

        print("end is: " + str(end))

        print("value is: " + str(value))

    @ddt.file_data('testdata_list.yml')

    def test_case_02(self, value):

        print("value is: " + str(value))

if __name__ == "__main__":
    unittest.main