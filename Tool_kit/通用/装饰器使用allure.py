# coding:utf-8
import pytest
import allure
import os
import subprocess

from commons.HandleJson import handle_json
import commons.configs as config
from commons.DBConn import DBConn
from commons.log import logger
from commons.HandleCompare import compareTest
from commons.ApiRequest import apiRequest
from SendEmail import send_mail

baseFileName = '../testdata/post_user_login_data.json'
testCaseData = handle_json.load_json(baseFileName)


@pytest.fixture()
def executeSql():
    logger.info("execute the sql")


# @pytest.mark.run(order=1)
@pytest.mark.usefixtures('executeSql')
@allure.feature('用户登录')
class TestUserLogin():
    @allure.title('用户登录接口')
    @allure.testcase('测试地址：http://127.0.0.1:5055')
    @allure.description('通过接口进行用户登录')
    @allure.step("第一步：用户登录")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def testUserLogin(self, case_data):
        api_response = apiRequest.api_request(config.apiurl, testCaseData, case_data)
        for case_validate in case_data['validate']:
            logger.info(
                '断言期望相关参数：check：{},comparator：{},expect：{}'.format(case_validate['check'], case_validate['comparator'],
                                                                   case_validate['expect']))
            compareTest.compare_Assert(api_response, case_validate['check'], case_validate['comparator'],
                                       case_validate['expect'])


if __name__ == "__main__":
    # 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
    # pytest.main(['-s', '-v', 'TestGetPropertyType.py','-q'])
    pytest.main(['-s', '-v', 'TestUserLogin.py', '-q', '--alluredir', 'report1'])
    os.system('if exist "report1/htmls" (rd /s/q report1/htmls)')
    os.system('allure generate report1 -o report1/htmls --clean')
    send_mail("Liang.Wu@test.com", "api测试报告", "测试报告的访问地址为：http://desktop-fe56ou7:8881/index.html<br> 请在收到邮件后三十分钟内查看！")
    os.system('allure open -h 10.8.31.61 -p 8881 report1/htmls')