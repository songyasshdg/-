import os
import logging

# 最好走绝对路径  因为生成报告的时候 不走运行run文件的时候会重复生成一份日志在./run下面
LOG_FILE = "C:\\Users\\Administrator\\a\\Api\\loggins\\login\\Apist.log"
if not os.path.exists(os.path.dirname(LOG_FILE)):
    os.makedirs(os.path.dirname(LOG_FILE))


# """
# $ Usage:
#     from init_logger import Logger
#     logger = Logger(__name__).get_log()
# """


class Logger:
    def __init__(self, logger=None, level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.propagate = False  # 防止终端重复打印
        self.logger.setLevel(level)
        fh = logging.FileHandler(LOG_FILE, 'a', encoding='utf-8')
        fh.setLevel(level)
        sh = logging.StreamHandler()
        sh.setLevel(level)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.handlers.clear()
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        fh.close()
        sh.close()

    def get_log(self):
        return self.logger
