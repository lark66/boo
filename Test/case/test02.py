import requests
import json
import unittest
import ddt
#from BeautifulReport import  BeautifulReport bs bf
from  urllib import parse

@ddt
class Login(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    base_url ='http://192.168.0.185/'

    @ddt.file_data('23.yaml')

    def test_request(self,case):
        data_dict =json.load(case.data)
        resp =requests(method =case.method,url=case.url,header=case.header,cookie=case.cookie)
        print("statue_code:",resp.get_statue_code())
        try:
            self.assertEqual(case.expected, response.get_text())
        except AssertionError as e:
            print("断言错误")
            raise e




#发送一个带参数的get请求 resp=request.get(url=protocol+host+path,params=cotent)

#params 里面的content 是一个字典形式的参数，多个参数的格式 content={"key":"valuse","key2":"value2"}


#protocol="https://"
#host="192.168.0.185:7000"
#path ="/user/auth_create_user/"
#定义参数
#content={"currentCardNo":"2400000003892222227","productld":"2"}

#发送请求
#resp = requests.get(url=protocol+host+path,data=content)
#print(resp.url)
#print(resp.status_code)
#print(resp.json())
