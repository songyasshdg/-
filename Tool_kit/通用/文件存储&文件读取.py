# @classmethod
# def mobiles(self):
#     tel = random.choice(['134', '139', '137', '135', '150', '151', '157', '130', '132', '133', '153'])
#     list1 = []
#     for i in range(8):
#         list1.append(random.choice('0123456789'))
#     part = ''.join(list1)
#     mobile = tel + part
#     with open("C:\\Users\\Administrator\\a\\Api\\Test_Yaml\\mobile_yaml.yaml", "a") as f:
#         f.seek(0)  # 从0位置开始读取
#         f.truncate()
#         f.write(mobile)
#         return mobile
#
#
# @classmethod
# def read_mbiles(self):
#     f = open("C:\\Users\\Administrator\\a\\Api\\Test_Yaml\\mobile_yaml.yaml")
#     data = f.readlines()  # 按行读取list
#     f.close()  # 关闭
#     return data
