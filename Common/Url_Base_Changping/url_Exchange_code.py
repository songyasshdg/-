#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
"""
系统名称:产品运营系统
界面名称:单机兑换码V1
菜单位置:产品运营系统>产品管理>产品设置>单机兑换码V1
"""
import requests


class TestCnm:
    """
    这里的属性是全局使用的,my_Base文件直接调用,其他文件也可以调用,只需要继承Tsetcnm即可;
    """
    # 全局token
    tokens = None
    s = requests.session()
    base_urls = "http://192.168.1.38:6105"
    # 登录接口地址
    base_url_login = "/all/login"
    """
    登录接口
    """
    # 单机兑换码-生成兑换码接口-单个生成
    base_exchange_code = "/operate/exchangeCode/add"
    # 单机兑换码-生成兑换码接口参数-单个生成
    data_exchange_code = {"expire_time": "2022-06-20 00:00:00", "num": 1, "type": 1, "value": 0}
    """
    参数说明:
    token:必填
    expire_time:过期时间
    num:兑换次数
    type:类型1是代表一次使用, 类型2是代表多次使用
    value:兑换值
    """
    # 单机兑换码-查询兑换码地址
    base_exchange_code_s = "/operate/exchangeCode/list"
    # 单机兑换码-查询兑换码参数
    data_exchange_code_s = {"code": "", "code_value": "", "limit": 100, "order": "2", "start": "", "status": ""}
    """
    参数说明:
    token:必填
    code:兑换码
    code_value:兑换值
    limit:一页的数量
    order:排序
    start:当前页
    status:状态
    """
    # 单机兑换码-批量生成兑换码接口地址-批量生成
    base_exchange_code_ss = "/operate/exchangeCode/batchAdd"
    # 单机兑换码-批量生成兑换码接口参数-批量生成
    data_exchange_code_ss = {"expire_time": "2022-07-20", "generate_num": 3, "num": "1", "type": "2",
                             "value": "2"}
    """
    参数说明:
    token:必填 
    expire_time:过期时间
    generate_num:生成数量
    num:兑换次数
    type:类型1一次使用,2多次使用
    value:兑换值
    """
    # 单机兑换码-使用测试接口
    base_exchange_code_sss = "/operate/exchangeCode/usetest"
    # 单机兑换码-使用测试接口 参数
    data_exchange_code_sss = {"appid": "19075", "code": "4717091549", "deviceId": "test", "ver": "v1"}
    """
    参数说明:
    token:必填 
    appid:产品id
    code:兑换码
    deviceId:设备id
    ver:版本
    """
