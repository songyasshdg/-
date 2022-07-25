import pytest
import allure
from hamcrest import *
from Apis.Common.my_Base_Changping.my_json_yaml_excel import FileTools
from Apis.Common.my_Base_Changping.my_Base_Chanping import Test_Chan_ping
from Apis.Common.my_Base_Changping.my_assart_Changping import TestCsm


@allure.epic('单机兑换码模块')
class TestApt(Test_Chan_ping, TestCsm):
    """
    跟上文中打开json方式类似，如下所示
    art_data = yaml.load(open("../data/art_data.yaml","r",encoding="utf8"),Loader=yaml.FullLoader)
    打开并读取yaml文件的中art_data数据，这次使用with方式打开，这里只是说明还有另一种方式
    with open("C:\\Users\\Administrator\\a\\Apis\\Test_Yaml\\yaml\\yaml_cahngping.yaml", "r", encoding="utf8") as f:
    art_data = yaml.load(f.read(), Loader=yaml.FullLoader)
    """
    # 如果不使用FileTools文件的方法, 则使用上面注释的方式即可
    art_data = FileTools().yaml_file(filename="C:\\Users\\Administrator\\a\\Apis\\Test_Yaml\\yaml\\yaml_cahngping.yaml")

    @pytest.mark.parametrize("res_method,url_path,art_body,status_code,msg", art_data)
    def test_art(self, res_method, url_path, art_body, status_code, msg):
        res_url = self.base_urls + url_path
        r = self.request_tets(method=res_method, url=res_url, headers=self.headers(), data=art_body)
        assert self.assart(response=r)
        assert_that(r.text, contains_string("1")) and assert_that(r.text, contains_string("生成成功"))


if __name__ == '__main__':
    pytest.main(['-vs', 'test_yaml_Changping.py'])
