import allure
from hamcrest import *
from Apis.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping
from Apis.Common.my_Base_Changping.my_assart_Changping import TestCsm
from Apis.Common.my_Base_Changping.my_json_yaml_excel import FileTools
import pytest


@allure.epic("单机兑换码模块")
class TestAit(Test_Chan_ping, TestCsm):
    """
    打开并读取json文件的中art_data数据 最好走绝对路径 不然在cmd指令运行会报错 art_data = json.load(open(
    "C:\\Users\\Administrator\\a\\Apis\\Test_Json\\Json\\json_cahngping.json", "r", encoding="utf8"))
    如果不调用FileTools文件的方法, 则需要使用注释的方法即可
    """
    art_data = FileTools().json_file(filename="C:\\Users\\Administrator\\a\\Apis\\Test_Json\\Json\\json_cahngping.json")

    @pytest.mark.parametrize("res_method,url_path,art_body,status_code,msg", art_data)
    def test_art(self, res_method, url_path, art_body, status_code, msg):
        res_url = self.base_urls + url_path
        r = self.request_tets(method=res_method, url=res_url, headers=self.headers(), data=art_body)
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("生成成功"))


if __name__ == '__main__':
    pytest.main(['-vs', 'test_json_Chanping.py'])
