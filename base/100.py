import unittest    #单元测试模块
import HTMLTestRunner   #用来生成报告用
from BeautifulReport import BeautifulReport as bf   #好看的测试报告 bf是别名方便使用
class TestCalc(unittest.TestCase):   #继承 变为测试用例

   def setUp(self):
      print('setup123')

   def tearDown(self):
      print('teardown321')

   @classmethod  #定义类方法
   def setUpClass(cls):  #直接继承父类方法
      #在所有用例执行之前运行的
      print('setupclss')

   @classmethod
   def tearDownClass(cls):
      #在所有用例都执行完之后运行的
      print('teardownclass')

   def test_lu(self):   #用例执行顺序是按照首字母的顺序（在报告中可看出）
                      #通过‘’‘来加入用例描述  报告中就会加入用例描述
      print('aina')
      self.assertEqual(1,1)  #该子类没有  继承父类比较两个值  后面也可以再加参数作为提示信息。
   def test_zch(self):   #以test开头就可以运行用例  否则不会自动运行

      print('赵传慧')
      self.assertEqual(1,1,msg="没有问题")

#if __name__ == '__main__':
 #   unittest.main()
   #会运行当前python文件里面的所有测试用例  **运行时注意run  产生报告时不用该模式


## 1、先把所有的测试用例都放到用例集。用例集也做测试套件是用来存放测试用例的
##2、运行这些测试用例
##3、产生报告
suite = unittest.TestSuite()  #测试集合 存放用例 其实是一个list
suite.addTest( unittest.makeSuite(TestCalc) ) #把刚才写的用例加进来 **写入类名

#bf报告生成
run = bf(suite)  #实例化一下，他是一个类必须实例化使用
run.report(description='描述必须写',filename='test') #还可指定log位置等

#HtmlTESTRunner如何产生报告
# f = open('test.html','wb')  #以2进制模式 不考虑编码集的问题
# runner = HTMLTestRunner.HTMLTestRunner(f,title='双鱼座用例标题',description='这是用例描述')  #后面两个参数是非必须的
# runner.run(suite) #运行用例