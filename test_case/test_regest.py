#@coding=utf-8
'''
1.引入第三方库（cmd,,pip install requests）
2.准备数据
3.发送请求
4.获取响应结果
5.断言
'''
import requests,json
import unittest
#url ,data,header,cookis....
from common1.newphone import new_phone
import pytest


class Test_Regest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://101.43.204.2/index.php/User/signup'
        self.data = {'phone': '19111111120',
                      'password': 123456,
                      'yao_ma': 10086}

    def tearDown(self) -> None:
        pass

    def test_regest_cussess(self):
        ph=new_phone()
        self.data['phone']=ph
        #发送请求
        r=requests.post(url=self.url,data=self.data)
        r=json.loads(r.text)
        #断言
        self.assertEqual(r['msg'],'注册成功')

    def test_regest_re_run(self):

        #发送请求
        r=requests.post(url=self.url,data=self.data)
        r=json.loads(r.text)
        #断言
        self.assertEqual(r['msg'],'手机号已注册,请登录!')

    def test_regest_name_empty(self):
        self.data['phone']=''
        #发送请求
        r=requests.post(url=self.url,data=self.data)
        r=json.loads(r.text)
        #断言
        self.assertEqual(r['msg'],'手机号不符合规范!')
if __name__ == '__main__':
   pytest.main(['-vs','test_regest.py'])
