class bcolors:
    HEADER = '\033[95m'  # 紫色
    OKBLUE = '\033[94m'  # 蓝色
    OKGREEN = '\033[92m'  # 翠绿
    WARNING = '\033[93m'  # 浅黄色
    FAIL = '\033[91m'  # 红色
    ENDC = '\033[0m'  # 默认值
    BOLD = '\033[1m'  # 加粗
    UNDERLINE = '\033[4m'  # 下斜线


print(bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC)
