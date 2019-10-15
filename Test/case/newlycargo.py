import requests
import json
import  HTMLTestRunner
from demo import RunMain

class TestMethon(unnittest.TestCase):
    def setUp(self):
        self.run=RunMain()


# 新增商品接口
    def test_01(self):
        url =''
        data ={}
        resp = requests.post(url=protocol + host + path, data=content)
        protocol = "http://"
        host = "192.168.0.185:7000"
        path = "/cargo/{cargo_id}"
        content = {"name:00,barcode:,category_id:,product_model:"}

        print(resp.text)
        print(resp.url)
if __name__ == '__main__':
    filepath ="../report/htmlreport.html"
    fp =file (filrpath,'wb')#读写格式打开
    suite =unittest.TestSuite()
   # unittest.TextTestRunner().run()
  runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
  runner.run(suite)