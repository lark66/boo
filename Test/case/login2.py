# /usr/bin python
# coding=utf-8
from ruamel.yaml import  YAML

yaml =YAML()




f = open('/Users/aina/PycharmProjects/ROS/case/23.yaml',encoding ='utf-8')

df=f.read()
print(type(df))


res =yaml.safe_load(df)
print(res)
print(type(res))
