import time
import logging
import logging.handlers
import os

# 如果日志文件夹不存在，则创建
log_dir = "log-day"  # 日志存放文件夹名称
log_path = os.getcwd() + os.sep + log_dir
if not os.path.isdir(log_path):
    os.makedirs(log_path)
# logging初始化工作
logging.basicConfig()
# 定义一个logger，logger相当于一个记录日志的人
# myapp = logging.getLogger('myapp')
# #定义记录日志的级别
# myapp.setLevel(logging.INFO)
# 添加TimedRotatingFileHandler 这个就是logger需要记录日志的规则。
# 定义一个1天换一次log文件的handler
# 保留3个旧log文件
# handler定义规则
timefilehandler = logging.handlers.TimedRotatingFileHandler(log_dir + os.sep + "sec.log", when='S', interval=1,
                                                            backupCount=0, encoding='utf-8')
# 设置后缀名称，跟strftime的格式一样
timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
formatter = logging.Formatter(
    '%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')  # %(asctime)s - %(levelname)s: %(message)s
# 格式化规则
timefilehandler.setFormatter(formatter)
# 给记录员添加记录规则
# myapp.addHandler(timefilehandler)
logging.getLogger().addHandler(timefilehandler)
while True:
    time.sleep(1)
    logging.warning("test")
