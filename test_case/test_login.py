#@coding=utf-8
#引入unittest和pythest框架
import unittest,pytest,requests,json
from ddt import ddt ,data
from common1.read_csv import ReadCsv
# ddata=[['login001','登录成功测试',19111111116,123456,'登录成功','p1'],
#        ['login002','禁止登录的帐号登录失败测试','19271358647','123456','该账户已被禁止登录!','p2'],
#        ['login003','不存在的帐号登录失败测试','13088888888','123456','帐户名或密码错误','p2']]


ddata=ReadCsv('../test_data/login_testcase.csv')
print(ddata)
@ddt
class Test_Login_A(unittest.TestCase):
    def setUp(self) -> None:
        self.url='http://101.43.204.2/index.php/User/login'
        self.data={'phone':'19111111116',
              'password':'123456'}

    def tearDown(self) -> None:
        pass

    @data(*ddata)
    def test_login_A(self,aa):
        #print('传入的值：',aa)
        self.data['phone']=aa[2]
        self.data['password'] = aa[3]
        #发送请求
        r=requests.post(url=self.url,data=self.data)
        r=json.loads(r.text)
        #print('响应结果：',r)
        #断言
        self.assertEqual(aa[4],r['msg'])
if __name__ == '__main__':
    pytest.main(['-vs'])