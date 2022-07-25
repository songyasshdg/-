#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
import allure
import pytest
from hamcrest import *
from Apis.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping
from Apis.Common.Url_Base_Changping.url_Exchange_code import TestCnm
from Apis.Common.my_Base_Changping.my_assart_Changping import TestCsm
import pytest_check as check


@allure.epic("单机兑换码模块")  # 一个模块构建一个类
class TestArt(Test_Chan_ping, TestCnm, TestCsm):
    @allure.feature("单机兑换码-单个生成")
    @allure.title('单机兑换码用例1-正向')
    @allure.description('接口地址:/operate/exchangeCode/add')
    @pytest.mark.flaky(reruns=2, reruns_delay=6)  # 如果用例执行失败,则重跑两次,每次延迟6秒
    def test_01(self):
        urls = self.base_urls + self.base_exchange_code
        r = self.request_tets(method='post', url=urls, data=self.data_exchange_code, headers=self.headers())
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("生成成功"))
        assert "1" and "生成成功" in r.text
        assert "生成成功" in r.text
        assert "1" in r.text  # 多层断言
        check.is_in("1" and "生成成功", r.text)
        check.is_in("1", r.text)
        check.is_in("生成成功", r.text)  # 多结构断言

    @allure.feature("单机兑换码-查询")
    @allure.title('单机兑换码用例2-正向')
    @allure.description('接口地址:"/operate/exchangeCode/list"')
    @pytest.mark.flaky(reruns=2, reruns_delay=6)
    def test_02(self):
        urls = self.base_urls + self.base_exchange_code_s
        r = self.request_tets(method='post', url=urls, data=self.data_exchange_code_s, headers=self.headers())
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("操作成功"))  # 效验返回的文本是否包含正确的参数

    @allure.feature("单机兑换码生成-批量生成")
    @allure.title('单机兑换码用例3-正向')
    @allure.description('接口地址:/operate/exchangeCode/batchAdd')
    @pytest.mark.flaky(reruns=2, reruns_delay=6)
    def test_03(self):
        urls = self.base_urls + self.base_exchange_code_ss
        r = self.request_tets(method='post', url=urls, data=self.data_exchange_code_ss, headers=self.headers())
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("生成成功"))  # 效验返回的文本是否包含正确的参数
        with open(r'C:\Users\Administrator\a\Apis\导出api\单机兑换码导出接口.xlsx', 'wb') as f:  # 将返回的数据写入文件 走绝对路径,不然生成报告会报错
            f.write(r.content)

    @allure.feature("单机兑换码-使用测试接口")
    @allure.title('单机兑换码用例4-正向')
    @allure.description('接口地址:/operate/exchangeCode/usetest')
    @pytest.mark.skip("单机兑换码测试服未配置使用不了(需要生成的兑换码需要刷新缓存才能生效), 正式服是OK的")
    @pytest.mark.flaky(reruns=2, reruns_delay=6)
    def test_04(self):
        urls = self.base_urls + self.base_exchange_code_sss
        r = self.request_tets(method='post', url=urls, data=self.data_exchange_code_sss, headers=self.headers())
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1"))


if __name__ == '__main__':
    pytest.main(['-vs', 'test_Exchange_code.py'])
