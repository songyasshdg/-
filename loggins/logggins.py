import logging.handlers
import logging

# 创建日志
logger = logging.getLogger("产品运营系统日志")
# 设置日志器的级别
logger.setLevel(logging.DEBUG)
# 创建两个处理器(一个输出到文件/一个输出到控制台)
sf = logging.StreamHandler()
# 创建输出到文件的处理器     when是代表时间   interval代表切割文件的时间  backupCount是代表备份几个文件
hf = logging.handlers.TimedRotatingFileHandler("./login/Changping.log", when='M', interval=1, backupCount=3)
# 设置日志级别
sf.setLevel(logging.INFO)
sf.setLevel(logging.DEBUG)
hf.setLevel(logging.INFO)
hf.setLevel(logging.DEBUG)
# 创建格式器
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
formatter = logging.Formatter(fmt=fmt)
# 添加格式器到处理器中
sf.setFormatter(formatter)
hf.setFormatter(formatter)
# 将处理器添加到日志器
logger.addHandler(sf)
logger.addHandler(hf)
logger.info("44444444444444444")
logger.debug("444444444adas444")
logger.error("4")
logger.warning("0")
