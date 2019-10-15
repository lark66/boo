import requests
import json

class TestMethon(unnittest.TestCase):
    def setUp(self):
        print('ceshi')

#  查询所有商品
    def token01(self):
        resp = requests.post(url=protocol + host + path, data=content)
        protocol = "http://"
        host = "192.168.0.185:7000"
        path = "/cargo/{cargo_id}"
        content = {"cargo_id:00"}
        print(resp.text)
        print(resp.url)