#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
import allure
import pytest
from hamcrest import *
from Apis.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping
from Apis.Common.my_Base_Changping.my_assart_Changping import TestCsm


@allure.epic("单机兑换码模块")
class TestAit(Test_Chan_ping, TestCsm):
    art_data = [("post", "/operate/exchangeCode/add", {"expire_time": "2022-06-20", "num": 1, "type": 1, "value": 0},
                 200, "生成成功"),
                ("post", "/operate/exchangeCode/add", {"expire_time": "2022-06-20", "num": 1, "type": 1, "value": 0},
                 200, "生成成功"),
                ("post", "/operate/exchangeCode/add", {"expire_time": None, "num": 1, "type": 1, "value": 0}, 200,
                 "生成成功"),
                ("post", "/operate/exchangeCode/add", {"expire_time": None, "num": 1, "type": 1, "value": 0}, 200,
                 "生成成功"), ]

    # @pytest.mark.skip(reason="就是不想执行而已!!!!!!!!!!!")  # 直接跳过
    @pytest.mark.flaky(reruns=2, reruns_delay=3)  # 如果执行失败 则重新重跑两次  延迟3秒
    # @allure.title("登录用例01")  如果要次功能  下面参数就不能使用ids 如果不用ids  就可以使用title  两者冲突一起使用值显示一个
    @pytest.mark.parametrize("res_method,url_path,art_body,status_code,msg", art_data, ids=[
        "用例1-输入正确账户,登录成功",
        "用例2-输入正确账户,登录成功",
        "用例3-输入正确账户,登录成功",
        "用例4-输入正确账户,登录成功"])
    def test_r(self, res_method, url_path, art_body, status_code, msg):  # 参数同步到方法中
        res_url = self.base_urls + url_path  # url_path 由域名拼接api地址组成
        r = self.request_tets(method=res_method, url=res_url, headers=self.headers(), data=art_body)
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("生成成功"))



if __name__ == '__main__':
    pytest.main(["-vs", "test_Csv_Cahngping.py"])
