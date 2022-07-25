#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
from Apis.loggins.llogin import Logger
from Apis.loggins.my_logins import logger
logger1 = Logger(__name__).get_log()


class TestCsm:
    @classmethod
    def assart(cls, response=None):
        try:
            if response.status_code == int(200) and response.json()['msg'] == '操作成功':
                logger.info(f"响应状态码:{response.status_code}, 状态描述:{response.json()['msg']}")
                return True
            elif response.status_code == int(200) and response.json()['msg'] == '生成成功':
                logger.info(f"响应状态码:{response.status_code}, 状态描述:{response.json()['msg']}")
                return True
            elif response.status_code != int(200) and response.json()['msg'] != '生成成功':
                logger.info(f"响应状态码:用例断言失败, 状态描述:用例断言失败")
                return False
            else:
                logger.info(f"响应状态码:用例断言失败, 状态描述:用例断言失败")
                print("------------断言错误,请检查!!!--------------")
        except AttributeError:
            logger.info(f"响应状态码:用例断言失败, 状态描述:用例断言失败")
            print("请求方法未定义,请检查!!!!!!!!")
            return False
        except KeyError:
            logger.info(f"响应状态码:用例断言失败, 状态描述:用例断言失败")
            print("请求方法未定义,请检查!!!!!!!!")
            return False
        except AssertionError:
            logger.info(f"响应状态码:用例断言失败, 状态描述:用例断言失败")
            print("请求方法未定义,请检查!!!!!!!!")
            return False
