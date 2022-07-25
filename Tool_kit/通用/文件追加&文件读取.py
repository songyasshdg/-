# Python 追加写入文件：
# #写txt文件追加
# def writetxt_a(txt,path):
#     with codecs.open(path,'a','utf-8') as w:
#         w.write(txt)
# 那么再次调用该函数时，如何清除原有文本内容呢？
# 解决方法
# #写txt文件追加
# def writetxt_a(txt,path):
#     with codecs.open(path,'a','utf-8') as w:
#         w.seek(0)	# 定位
#         w.truncate()  # 清空文件
#         w.write(txt)
# f.seek(0)：把文件定位到数据起始位置（index=0），若没有这句的话，文件则默认定位到数据结束位置，w.truncate()不起作用。
# w.truncate()：从**位置（index）**处清空文件内容




# 读取--------------------------------
# 方法1：
# f=open('唐诗一百首.txt', encoding='gbk')
# txt=[]
# for line in f:
#     txt.append(line.strip())
# print(txt)
# 方法2
# f=open('唐诗一百首.txt')
# line = f.readline().strip() #读取第一行
# txt=[]
# txt.append(line)
# while line:  # 直到读取完文件
#    line = f.readline().strip()  # 读取一行文件，包括换行符
#    txt.append(line)
# f.close()  # 关闭文件
# print(txt)
# 方法3
# f=open('唐诗一百首.txt')
#
# data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
# 
# f.close()  # 关
# print(data) #返回list
# 方法4
# import numpy as np
#
# data = np.genfromtxt("文档练手.txt",dtype=[int, float,int])  # 将文件中数据加载到data数组里
# print(data)
