import  unittest
import ddt
import  requests




@ddt.ddt
class MyTest(unittest.TestCase):
    #初始化
    def setUp(self):
        print('setup')


 #   @ddt.data([1,2,3],[0,0,0],[999,1,1000])
    @ddt.file_data('ceshi1.yaml')
    @ddt.unpack
    def test_login(self,**kwargs):
        url =kwargs.get('url')
        method =kwargs.get('method')
        data =kwargs.get('data',{})

        header =kwargs.get('header',{})
        is_json =kwargs.get('is_json',{})
        cookie =kwargs.get('cookie',{})

        if method =='get':
            res =request.get(url=url,params=data,cookies=cookie,header=header)
            #self.assertIn(check,res)
            print(res.json())
        else:
            if is_json ==1:
                res =requests.post(url=url,json=data,cookies=cookie,header=header)
                print(res.json())
                #self.assertIn(check, res)
            else:
                res =requests.post(url=url,data=data,cookies=cookie,header=header).text
                print(res.json())
               # self.assertIn(check,res)

    def tearDown(self):
        print('teanDown')


if __name__ == '__main__':
    unittest.main()