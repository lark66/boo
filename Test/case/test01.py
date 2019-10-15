import unittest
import requests
import HTMLTestRunner

import yaml

class MyTest(unittest.TestCase):


    #每次方法之前执行

    def setUp(self):
        print('setup 02')
    #每次方法之后执行

    def tearDown(self):
        print('testDown03')

    @classmethod
    def setUpClass(cls):  # 所用用例执行之前执行
        print('类执行之前的方法')

    @classmethod
    def tearDownClass(cls):  # 所用用例执行之后执行

        print('01')

    def test_01(self):

        url='http://192.168.0.185:7700/auth/token/?token=cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5'
       # content ={'token':'cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5'}
        resp=requests.post(url)
        print(resp.url)

#unittest.main()
suite = unittest.TestSuite()#测试集合
tsuite.addTest(unittest.makeSuite('MyTest'))
'''f = open('report.html','wb') #打开一个文件

#定义一个运行的人  runner，stream=f  是将结果保存在该文件中，title 表示报告标题
runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                       title='b报告',
                                       description='报告描述')
runner.run(test_suite) #使用runner 运行测试集合中用例
f.close() #关闭打开的文件'''
#好看的报告
run = bf(suite)
run.report(description='描述'，filename='test')






if __name__ == '__main__':
    unittest.main()