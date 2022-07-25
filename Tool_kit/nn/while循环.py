"""
======================
Author: 柠檬班-小简
Time: 2021/1/13 20:45
Project: py37-编程基础
Company: 湖南零檬信息技术有限公司
======================
"""
"""
循环 -  上班/下班

while
for

while 毕业：
    上班
    直到年龄为60岁：
        再见，不上了！

while 条件:
    条件为真，会执行的代码。
    直到有一个条件不满足:
        退出循环(break)

死循环：写代码的时候，一定要避免死循环。
       第一种：在while运行的过程当中，改变了条件中用的数据/变量。总有一次让while的条件不成立
       第二种：使用break

while的特点：
    由条件来决定循环次数。
    当我们的应用场景，不确定循环次数的时候，使用while
"""
# while True:
#     print("66666")

score = int(input("请输入一个数字: "))
# while score >= 80:
#     print("优秀优秀！！！")
#     score -= 1  # 在while运行的过程当中，改变了条件中用的数据/变量。总有一次让while的条件不成立。
#     if score == 85:
#         break  # 退出while循环

# while score in [87,88,89,90]:
#     if score < 90:
#         break


