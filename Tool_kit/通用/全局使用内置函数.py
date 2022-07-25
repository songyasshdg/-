# import json
# import pytest
# from Api.Common.my_Base import TestCom
# from Api.Common.my_Base_Url import TestCnm
# from Api.Common.my_Assert import TestCsm
# import allure
#
#
# class TestArt(TestCom, TestCnm, TestCsm):
#     @allure.epic("登录模块")
#     @allure.feature("用例1-正向")
#     @pytest.mark.skip("就是不想执行---------")
#     @pytest.mark.flaky(reruns=2, reruns_delay=3)
#     def test_01(self):
#         r_url = self.base_urls + self.base_url_address
#         r = self.request_tets(method="post", url=r_url, headers=self.headers(), json=self.r_datas_oder)
#         assert self.assart(responses=r)
#
#     @allure.epic("注册模块")
#     @allure.feature("用例2-逆向")
#     @pytest.mark.flaky(reruns=2, reruns_delay=3)
#     def test_02(self):
#         r_url = self.base_urls + self.base_url_code
#         r_datas = {"mobile": self.mobiles()}
#         json.dumps(r_datas)
#         r = self.request_tets(method="post", url=r_url, data=r_datas)
#         str_id = str(r.json()['data'])
#         globals()['ids'] = str_id
#         assert self.assart(responses=r)
#
#     @allure.epic("注册模块")
#     @allure.feature("用例1-正向")
#     @pytest.mark.flaky(reruns=2, reruns_delay=3)
#     def test_03(self):
#         r_url = self.base_urls + self.base_url_register
#         r_datas = {"mobile": self.read_mbiles(), "smsCode": globals()['ids']}
#         json.dumps(r_datas)
#         r = self.request_tets(method="post", url=r_url, data=r_datas)
#         assert self.assart(responses=r)
#
#
# if __name__ == '__main__':
#     pytest.main(['-vs', 'test_linjiashop.py'])