#@coding=utf-8
import requests
import pytest
from config.urladdress import url1
def test_loadimage_cussess_png():

    url =url1

    payload = {}
    files=[
      ('imgFile',('身份证2.png',open('../imagefiles/1.png','rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    assert 1==1


def test_loadimage_cussess_jpg():

    url =url1

    payload = {}
    files=[
      ('imgFile',('身份证2.png',open('../imagefiles/1.png','rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    assert 1==1


if __name__ == '__main__':
    pytest.main(['-vs','test_loadfile.py'])
