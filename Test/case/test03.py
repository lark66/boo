import requests
import yaml

fp = open("/Users/aina/PycharmProjects/ROS/case/info.yaml")
req = yaml.load(fp)
fp.close()
print(type(req))
print(req)

import json
#form  类型参数发送post


url = req['url']
content ={}
#发送post
resp =requests.post(url=url,data=content)

print(resp.url)
print(resp.status_code)
print(resp.json())
print(type(resp.json()))
print(resp.json()['errorCode'])
print(resp.json()['errorMessage'])
print(resp.json()['data'])
print(type(resp.json()['data']))
print(resp.json()['error'])