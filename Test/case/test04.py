import requests
import json
#post 请求的body是json 类型 ，需要用json 参数传入，需要先导入jsonmok ，用dumps 方法转化橙json 然后传给data


def
dictData={"":","":""}
dataJson=json.dumps(dictData)


print(dataJson)

#d定义resp 变量获取请求json 类型入参 的接口返回值

resp=requests.post(url='https://httpbin,org/post',data=dataJson)


#打印返回值的状态玛
print(resp.status_code)
#打印返回值
print(resp.txt)
