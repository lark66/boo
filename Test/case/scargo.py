import requests


#查询车辆详细信息接口
url ="http://192.168.0.185:7700/data/vehicles/"
resq = requests.get(url,params={'token':'cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5'})
result = resq.json()
print (result)

#断言接口返回值

assert result['code'] == 3009
assert result['detail'] == 'token检测失败,token不存在'
#assert result['data']['synthesis_detail']=""







