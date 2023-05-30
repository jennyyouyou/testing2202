#@coding=utf-8
from random import randint,choice
'''生成手机号码的函数'''
def new_phone():
    #获取手机号码的前两位
    phone1=choice(['13','14','15','16','17','18','19'])
    #生成手机号码的后8位
    phone2=str(randint(100000000,999999999))
    #拼接成为手机号码
    ph=phone1+phone2
    #返回手机号码
    return(ph)
