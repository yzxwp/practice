# author:闫振兴
# contact: 1753502691@qq.com
# datetime:2020/6/29 8:41
# software: PyCharm
"""
文件说明：
"""

# encoding:utf-8
import requests
import json
import unittest
from ddt import ddt, file_data
from python_requests import config


@ddt
class MyTestCase(unittest.TestCase):
    @file_data("test_phone.json")
    def test_case01_phoneAPI(self, phone, key, province):
        url = "http://" + config.host + "/" + config.MOBILE
        querystring = {"phone": phone, "key": key}
        headers = config.heard
        response = requests.request("GET", url, headers=headers, params=querystring)
        json_ret = json.loads(response.text)
        act = [json_ret["resultcode"], json_ret["result"]["province"]]
        exp = ["200", province]
        print(json_ret)
        # print(json_ret["resultcode"])
        # print(json_ret["result"]["zip"])
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main()
