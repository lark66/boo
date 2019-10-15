import  unittest
from  module import  Calculator

class ModuleTest(unittest.TestCase):
    def setUp(self):
        self.cal =Calculator(9,3)
    def tearDown(self):
        pass
    def test_add(self):
        result =self.cal.add()
        self.assertEqual(result,12)
if __name__ == '__main__':
    unittest.main()

    #构造测试集
    suite=unittest.TestCase()
    suite.addTest(ModuleTest("test_add"))


    #执行测试
    runner =unittest.TextTestRunner()
    runner.run(suite)
