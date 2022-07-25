import logging.handlers
import os

logger = logging.getLogger("产品运营系统")
logger.setLevel(logging.INFO)
# 创建输出到文件的处理器     when是代表时间   interval代表切割文件的时间  backupCount是代表备份几个文件
fh = logging.handlers.TimedRotatingFileHandler("./login/Apitest.log", encoding="utf-8", when="s", interval=1,
                                               backupCount=2)
sf = logging.StreamHandler()
logger.propagate = False
fmt = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
fh.setFormatter(fmt)
sf.setFormatter(fmt)
logger.addHandler(sf)
logger.addHandler(fh)
log = os.path.join(os.path.dirname(__file__))  # 获取当前路径，返回上一级进入logs目录
if not os.path.exists(log):  # 如果logs目录不存在，就先创建logs目录
    os.mkdir(log)
logfiles = os.path.join(log, "Apitest.log")
re = logging.FileHandler(logfiles)  # 日志记录到指定文件中
re.setFormatter(fmt)  # 输出日志使用定义的format格式
logger.addHandler(re)  # 日志输出到控制台
