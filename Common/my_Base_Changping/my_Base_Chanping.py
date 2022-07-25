#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
import random
import requests
from Apis.loggins.my_logins import logger


class Test_Chan_ping():
    tokens = None  # 全局token
    s = requests.session()  # 全局session
    base_urls = "http://192.168.1.38:6105"  # 全局域名

    @classmethod
    def setup_class(cls):
        base_urls = cls.base_urls + "/all/login"
        login_data = {"value": "eyJ1bmFtZSI6InNvbmd5YSIsInB3ZCI6InNvbmd5YTA2MTAifQ=="}
        r_login = cls.s.post(url=base_urls, data=login_data)
        cls.tokens = r_login.json()['token']

    @classmethod
    def headers(self):
        header = {"token": self.tokens, 'charset': 'UTF-8'}
        return header

    @classmethod
    def headers_json(self):
        header_json = {"token": self.tokens, 'Content-Type': 'application/json', 'charset': 'UTF-8'}
        return header_json

    @classmethod
    def mobiles(self):
        tel = random.choice(['134', '139', '137', '135', '150', '151', '157', '130', '132', '133', '153'])
        list1 = []
        for i in range(8):
            list1.append(random.choice('0123456789'))
        part = ''.join(list1)
        mobile = tel + part
        with open(r"C:\Users\Administrator\a\Api\Test_yaml\mobile_yaml.yaml", "a") as f:  # 使用转义符 r  或者加\\
            f.seek(0)  # 从0位置开始读取
            f.truncate()
            f.write(mobile)
            return mobile

    @classmethod
    def read_mbiles(self):
        f = open(r"C:\Users\Administrator\a\Api\Test_yaml\mobile_yaml.yaml")
        data = f.readlines()  # 按行读取list
        f.close()  # 关闭
        return data

    @classmethod
    def upload_file(self, filename, filepath, filetype):
        """

        :param filename: 文件的名称+格式
        :param filepath: 文件的路径
        :param filetype: 文件的媒体类型
        :return: rb 表示二进制方式读取
        """
        files_data = {"file": (filename, open(filepath, "rb"), filetype)}
        return files_data

    @classmethod
    def bcolors(self, bcolor=None):
        self.HEADER = '\033[95m'  # 紫色
        self.OKBLUE = '\033[94m'  # 蓝色
        self.OKGREEN = '\033[92m'  # 翠绿
        self.WARNING = '\033[93m'  # 浅黄色
        self.FAIL = '\033[91m'  # 红色
        self.ENDC = '\033[0m'  # 默认值
        self.BOLD = '\033[1m'  # 加粗
        self.UNDERLINE = '\033[4m'  # 下斜线
        bcolors_data = bcolor.OKGREEN + {} + bcolor.ENDC
        return bcolors_data

    @classmethod
    def request_tets(self, method: str, url, params=None, data=None, json=None, headers=None, files=None,
                     **kwargs):  # 自定义发送请求
        """自定义发送请求
        请求方法为字符串格式，params、data、json,headers,files数据可以为空
        method：请求方法
        url：请求URL
        params：get请求的参数
        data：body中的数据
        json：body中json格式的数据
        kwargs：其它字典参数，允许传入不定长的参数
        logger.info(f"请求方法：{method},请求地址：{url},请求参数：{res.request.body},响应结果：{res.text}") 最开始的方法
        """
        method = method.upper()  # 将请求方法转换成大写
        if method == "GET":  # 当请求方法为GET时，调用requests库中的get请求
            res = self.s.get(url, params=params, headers=headers, files=files, **kwargs)
            logger.info('\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n响应拼接参数：{res.request.body}\n请求头:{headers}\n上传文件:{files}\n\n\n\n响应结果：{res.text}\n\n")
            # logger.info(f"请求方法：{method},请求地址：{url},请求参数：{res.request.body},响应结果：{res.text}")
            return res  # 返回请求
        elif method == "POST":  # 当请求方法为POST时，调用requests库中的POST请求
            res = self.s.post(url, data=data, json=json, headers=headers, files=files, **kwargs)
            logger.info('\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n响应拼接参数：{res.request.body}\n请求头:{headers}\n上传文件:{files}\n\n\n\n响应结果：{res.text}\n\n")
            return res
        elif method == "PUT":  # 当请求方法为PUT时，调用requests库中的PUT请求
            res = self.s.put(url, data=data, json=json, headers=headers, files=files, **kwargs)
            logger.info('\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n响应拼接参数：{res.request.body}\n请求头:{headers}\n上传文件:{files}\n\n\n\n响应结果：{res.text}\n\n")
            return res
        elif method == "DELETE":  # 当请求方法为DELETE时，调用requests库中的DELETE请求
            res = self.s.delete(url, data=data, json=json, headers=headers, files=files, **kwargs)
            logger.info('\n'f"请求方法：{method}\n请求地址：{url}\n请求参数:{data}\n响应拼接参数：{res.request.body}\n请求头:{headers}\n上传文件:{files}\n\n\n\n响应结果：{res.text}\n\n")
            return res
        else:  # 如果不是以上4种请求方法，则提示"请求方法未定义，请检查！"
            print("请求方法未定义，请检查！")
