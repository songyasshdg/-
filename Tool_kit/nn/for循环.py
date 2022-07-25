"""
======================
Author: 柠檬班-小简
Time: 2021/1/13 21:16
Project: py37-编程基础
Company: 湖南零檬信息技术有限公司
======================
"""
"""
for循环 - for遍历 - 列表/字典/元组/字符串

py37 - 列表 - 116个成员
老师遍历这个列表，与每个成员打个招呼。

遍历：从头到尾访问一遍。

语法:

for 变量名 in 列表/字典/元组/字符串:
    取到每一个成员后，会执行的代码(会做的事情)
    
for后面的变量名，取出来的每一个值，都会用变量名去接收

break: 退出循环
continue: 跳过本轮循环，不执行continue之后的代码。直接进入下一轮循环

上班、离职(break)、请假(continue)
每天都要做的事情：上班
某一天你生病了：那一天的班你就没上。仅限于那一天，跳过那一天的班。第二天还得继续干。

离职：再见，再也不来了。

for循环：
   遍历次数是：列表/字典/元组/字符串的长度。

遍历次数 - 固定/不固定
死循环 - 
避免死循环 - 循环条件的变更

列表和字典的遍历
# 1、遍历列表的值(成员)
# 2、遍历列表的下标，通过下标去取值

有一个生成整数列表的方法：range
range([起始整数],结束整数,[步长])   起始整数默认为0，步长默认为1  左闭右开(取头不取尾)
range(5) => [0,1,2,3,4]
range(1,5) => [1,2,3,4]
range(1,10,2)  => [1,3,5,7,9]


字典的遍历：
字典的成员 key-value

1、遍历key
for key in dict.keys()

2、遍历key-value
for item in person_info.items():
    print(item)

for key,value in person_info.items():
    print(key,value)


"""
new_list = ["玖yue", "柠檬", "人生", "leisen", "Bodhi", "饭团"]
#
# # 1、遍历列表的值(成员)
# for item in new_list:
#     print(f"哈罗，{item}")
#     if item == "人生":
#         continue
#
# # 2、遍历列表的下标，通过下标去取值 [0,1,2,3...]
# for index in range(len(new_list)):
#     # print(index) # 索引
#     # print(new_list[index]) # 索引对应的值
#     print("索引为 {} 的值是: {}".format(index,new_list[index]))


person_info = {"name": "xj", "age":18, "city": "长沙", "girl": ""}
# for key in person_info.keys():
#     print(key)

print(person_info.items())

for item in person_info.items():
    print(item)

for key,value in person_info.items():
    print(f"{key}: {value}")






# 计算1，，，100的和。
# sum = 1 +2 +3 +4 +5+ .. 100
# 怎么样去生成一个1，2，3，4，。。。100的列表
# sum = 0
# for i in range(1,101):
#     print(i)
#     sum += i
# print("sum为：",sum)

