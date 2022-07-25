#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com

import pytest
import requests
from Apis.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping


class Testai(Test_Chan_ping):
    s = requests.session()  # 全局保存会话
    __base_url = "https://edc.vimedia.cn:6115"  # 全局域名
    token = ""  # 全局token

    def test_001(self):
        base_urls = self.__base_url + "/all/login"
        login_data = {"value": "eyJ1bmFtZSI6InNvbmd5YSIsInB3ZCI6InNvbmd5YTA2MTAifQ=="}
        r = self.request_tets(method="post", url=base_urls, data=login_data)
        assert r.status_code == 200
        assert r.json()['msg'] == 'success'

    def test_002(self):
        base_urls = self.__base_url + "/all/login"
        login_data = {"value": "eyJ1bmFtZSI6InNvbmd5YSIsInB3ZCI6InNvbmd5YTA2MTAifQ=="}
        r = self.request_tets(method="post", url=base_urls, data=login_data)
        assert r.status_code == 200
        assert r.json()['msg'] == 'success'


if "__name__" == "__main__":
    pytest.main(['-vs', 'test_Debug.py'])
data = {"userid": "100086", "lsn": "454548", "pid": "37696052", "appid": "37696", "aid": "", "idfa": "", "timestamp": "", "sign": ""}
