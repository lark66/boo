
import yaml

fp = open("/Users/aina/PycharmProjects/ROS/case/login.yaml")
req = yaml.safe_load(fp)
print(req)



#封装auth/signin_form/ 用户密码登录
class RunMain:
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)

    def senf_get(self,url,data=None):
        res = requests.get(url=url,data=data,).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def send_post(self,url,data=None):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)
    def run_main(self,url,method,data=None):
        res = None
        if  method == 'GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res
if __name__ == '__main__':

    #token 检测
    url =  'http://192.168.0.185:7700/auth/signin_form/'

    data={
        'username':'admin',
        'password':'123456',
        'type':'password',
        'secyrity':'',
        'token':'cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5'

    }
    run = RunMain(url,'POST',data=data)
  #  self.assertEqual(run['errorcode'],1000,)
    print(run.res)