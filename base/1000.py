import unittest, requests

import ddt  # #可做参数化  自动读文件中数据

from BeautifulReport import BeautifulReport as bf

from urllib import parse


@ddt.ddt  # 申明这个类要别ddt使用啦
class Login(unittest.TestCase):
    base_url = 'http://192.168.0.185:7700/'  # 为给url统一加前缀   可写入配置文件比较好

    @ddt.file_data(
        'ceshi1.yaml')  # ddt帮你读文件，获取文件内容，循环调用函数，并且传给下面函数的如kwargs中，有多少条数据循环调用多少次下面的函数  注意修改文件open源码加入utf8编码打开不报错
    def test_request(self, **kwargs):

        detail = kwargs.get('detail', '没写用例描述')  # '''和%s组合来描述用例在这里无效。

        self._testMethodDoc = detail  # 动态的用例描述

        url = kwargs.get('url')  # url

       # url = parse.urljoin(self.base_url, url)  # 拼接好url  只能拼接 比如关于/的问题处理

        method = kwargs.get('method', 'get')  # 请求方式给他一个默认值get  防止没有传请求方式

        data = kwargs.get('data', {})  # 请求参数

       # header = kwargs.get('header', {})  # 请求头

       # cookie = kwargs.get('cookies', {})  # cookie

        check = kwargs.get('check')

        method = method.lower()  # 便于处理

        try:

            if method == 'get':

                res = requests.get(url, params=data).text
                self.assertIn(c, res, msg='预计结果不符，预期结果【%s】,实际结果【%s】' % (c, res))

                # 因为接口有异常的情况下， 可能返回的不是json串，会报错

            else:

                res = requests.post(url, data=data).text
                self.assertEqual()
                self.assertIn(c, res, msg='预计结果不符，预期结果【%s】,实际结果【%s】' % ( c, res))

        except Exception as e:

           print('')

           res = e

        for c in check:
            self.assertIn(c, res, msg='预计结果不符，预期结果【%s】,实际结果【%s】' % (
            c, res))#查看是否包含 断言查看一次错误就停止，后面加如错误提示  但check在yml中得是list方便查看是否包含。


sutie = unittest.TestSuite()

sutie.addTest(unittest.makeSuite(Login))  # 添加用例

#bf 报告生成
run = bf(sutie)  # 实例化  它是一个类  必须实列化使用

run.report('login_test', 'token检测')

print(run.success_count)  # 通过的次数

print(run.failure_count)  # 失败的次数