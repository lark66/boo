import yaml

f = open('/Users/aina/PycharmProjects/ROS/case/info.yaml')
print(yaml.safe_load(f))





class Person(object):

    def __init__(self,url,headers,data,Method):
        self.url = url
        self.headers =headers
        self.data =data
        self.Method=Method
    def person_cons(loader,node):
        value = loader.construct_mapping(node)
        url =value['url']
        headers =value['headers']
        data =value['data']
        Method =value['Method']
        return Person(url,headers,data,Method)

class TestSend(object):
    def __init__(self, config_path, cookie1=None, session1=None):
        #EnvParameter.__init__(self,conpath=None ,url=None,method=None,header=None,type=None,data=None,param=None,json=None,cookies=None,session=None)
        object.__init__(self, config_path)
        self.session = session1
        self.cookie1 = cookie1
        print(self.param,self.type) #测试下类继承效果

    def send(self):
        if self.method.upper() == "GET":
            rep = TestApi().get(self.url, self.param, self.header, cookie=self.cookie1, session=self.session)
            return rep
        elif self.method.upper() == "POST":
            rep = TestApi().post_data(self.url, self.type, self.data, self.header, cookie=self.cookie1,
                                      session=self.session1)
            return rep
        elif self.method.upper() == "PUT":
            rep = TestApi().put(self.url, self.data, cookie=self.cookie1, session=self.session1)
            return rep
        elif self.method.upper() == "DELETE":
            rep = TestApi().delete(self.url, self.data, cookie=self.cookie1, session=self.session1)
            return rep


#if __name__ == "__main__":
#     TestSend('./conf.yaml')
