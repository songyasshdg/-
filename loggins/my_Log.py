"""
1）日志收集器
    定义日志收集器：要从代码当中按照要求 收集对应的日志，并输出到渠道当中。
    a、要收集哪个级别以上的日志？
    b、日志是要什么样的格式显示？
    c、日志要输出到哪些地方去？


2）日志级别(Level)：
     debug - info - warning -error - critical(FATA)
      调试    基本     警告     报错     严重错误
3）日志显示的格式(Formatter):
     时间、日志级别、代码文件、第几行:信息
4）日志输出渠道(Handle):
    文件(FileHandle)、控制台(StreamHandle)   
    
    
自定义日志收集：
1、调用logger = logging.getLogger(日志名字)来生成一个日志收集器对象
2、设置你的日志收集级别。logger.setLevel(日志级别),一般为INFO
3、使用logging.Formatter类来定制要输出到控制台/文件当中的日志格式
4、使用handle1 = logging.StreamHandle()来创建一个控制台渠道对象，
   并将控制台要输出的日志格式设置为3当中的formatter. 设置：handle1.setformatter(Formatter对象)
5、将4当中的handle1添加到logger当中，那么日志就可以输出到控制台。

6、使用handle2 = logging.FileHandle(日志文件路径)来创建一个控制台渠道对象，
   并将控制台要输出的日志格式设置为3当中的formatter. 设置：handle2.setformatter(Formatter对象)
7、将6当中的handle2添加到logger当中，那么日志就可以输出到文件当中。

6、使用handle3 = logging.FileHandle(日志文件路径)来创建一个控制台渠道对象，
   并将控制台要输出的日志格式设置为3当中的formatter. 设置：handle3.setformatter(Formatter对象)
   
   指定handle3的日志级别为ERROR
   handle3.setLevel(logging.ERROR)
   
7、将6当中的handle3添加到logger当中，那么日志就可以输出到文件当中。



"""
import logging

# 第一步：
# 创建一个日志收集器
import os

logger = logging.getLogger("产品运营系统")

# 第二步：
# 设自定义要收集的日志级别、自定义日志格式、自定义输出渠道

# 设自定义要收集的日志级别
logger.setLevel(logging.INFO)

# 自定义日志格式(Formatter)
fmt_str = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'

# 实例化一个日志格式类
formatter = logging.Formatter(fmt_str)

# 实例化渠道(Handle).
# 控制台(StreamHandle)
handle1 = logging.StreamHandler()
# 设置渠道当中的日志显示格式
handle1.setFormatter(formatter)

# 将渠道与日志收集器绑定起来
logger.addHandler(handle1)

# 文件渠道(FileHandle)
handle2 = logging.FileHandler("C:\\Users\\Administrator\\a\\Apis\\loggins\\login\\Apitest1.log", encoding="utf-8")
# 设置渠道当中的日志显示格式
handle2.setFormatter(formatter)
# 将渠道与日志收集器绑定起来
logger.addHandler(handle2)


# # 文件渠道(FileHandle)
# handle3 = logging.FileHandler("./login/Apitest2.log", encoding="utf-8")
# # 设置渠道当中的日志显示格式
# handle3.setFormatter(formatter)
# # 设置handle3的日志输出级别为ERROR
# handle3.setLevel(logging.ERROR)
#
# # 将渠道与日志收集器绑定起来
# logger.addHandler(handle3)

# # 文件渠道(FileHandle)
# handle4 = logging.FileHandler("./login/Apitest3.log", encoding="utf-8", )
# # 设置渠道当中的日志显示格式
# handle4.setFormatter(formatter)
# # 设置handle4的日志输出级别为ERROR
# handle4.setLevel(logging.ERROR)
#
# # 将渠道与日志收集器绑定起来
# logger.addHandler(handle4)

# logger.info("hello,logging!!")
# logger.warning("hello,warning!!")
# logger.error("你错了！！")
# logger.error("ssss")
log = os.path.join(os.path.dirname(__file__))  # 获取当前路径，返回上一级进入logs目录
if not os.path.exists(log):  # 如果logs目录不存在，就先创建logs目录
    os.mkdir(log)
logfiles = os.path.join(log, "C:\\Users\\Administrator\\a\\Apis\\loggins\\login\\Apitest1.log")
re = logging.FileHandler(logfiles)  # 日志记录到指定文件中
re.setFormatter(formatter)  # 输出日志使用定义的format格式
logger.addHandler(re)