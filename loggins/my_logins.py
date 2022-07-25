#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com
import logging.handlers
import os

logger = logging.getLogger("产品运营系统")  # 定义日志并设置名称然后赋值给logger
logger.setLevel(logging.DEBUG)  # 设置日志为DEBUG级别
# 创建输出到文件的处理器     when是代表时间   interval代表切割文件的时间  backupCount是代表备份几个文件
fh = logging.handlers.TimedRotatingFileHandler("C:\\Users\\Administrator\\a\\Apis\\loggins\\login\\Api.log",
                                               encoding="utf-8", when="s", interval=1, backupCount=2)
fh.setLevel(logging.DEBUG)
# 定义日志格式，输出格式为：当前时间 - 日志等级 - 函数名 - 日志信息
format = logging.Formatter(
    '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s''\n')
yd = logging.StreamHandler()  # 输出日志记录
yd.setFormatter(format)  # 输出日志使用定义的format格式
logger.addHandler(yd)  # 日志输出到控制台
# 定义日志存放目录
log = os.path.join(os.path.dirname(__file__))  # 获取当前路径，返回上一级进入logs目录
if not os.path.exists(log):  # 如果logs目录不存在，就先创建logs目录
    os.mkdir(log)
logfiles = os.path.join(log, "C:\\Users\\Administrator\\a\\Apis\\loggins\\login\\Api.log")
re = logging.FileHandler(logfiles)  # 日志记录到指定文件中
re.setFormatter(format)  # 输出日志使用定义的format格式
logger.addHandler(re)  # 日志输出到控制台
