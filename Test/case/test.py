import requests


def test_login():
    url =  'http://192.168.0.185:7700/auth/token/'
    method = 'POST'

    data = {"token": "cde7fb1e3f2db079f053483a93e4ca9f62373433dd683499db4de5f5"}
    resp = requests.request(method, url, headers=headers, data=data)
    print(resp.json())
    # 解码json格式数据
    dicts = json.loads(a.text)
    code = a.status_code
    # 对比返回值
    self.assertEqual(code, 200)
    self.assertEqual(dicts['status'], 'ok')
    self.assertEqual(dicts['error'], None)
