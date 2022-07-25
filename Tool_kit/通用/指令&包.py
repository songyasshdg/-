# 包名
# from selenium.webdriver.common.by import By  #selenium库  定位元素包
# import unittest   ##unittest框架包
# import time  #时间包
# from selenium.webdriver.common.keys import Keys   ##键盘包
# from selenium.webdriver.common.action_chains import ActionChains    ##鼠标双击包
# from selenium import webdriver  ##驱动包
# pip install paramunittest  参数化包
# pip install HTMLTestRunner-Python3  生成报告的html包
# pip  install  selenium 框架
# pip install -U pytest  pytest包
# 查看安装的pytest的版本
# pip install nose
# pip install ddt
# pip install openpyxl
# pip install allure-pytest
# pip install jsonpath
# 跨文件调用(以下举例)
# – src
# |-- mod1.py
# |-- lib
# | |-- mod2.py
# |-- sub
# | |-- test.py
# import sys
# sys.path.append("..")

# import mod1
# import mod2.mod2


# 指令 raise                        ("抛异常") self.driver.implicitly_wait(10) 隐式等待为10秒 driver.quit()  关闭浏览器 (关闭所有)
# driver.maximize_window()  ##最大化窗口 driver.get(url_)  ##获取网页 time.sleep(1.ini)  ##强制等待 driver.refresh()  ##刷新页面
# driver.back()  后退 driver.forward()  前进 driver.maximize_window()  窗口# 最大化 driver.minimize_window()  # # 最小化
# driver.set_window_size(height=600, width=800)  # # 设定窗口固定大小 driver.set_window_size(600, 800)  # 简写方式  设定窗口固定大小
# driver.close() # 关闭当前窗口 Jasminum.switch_to.window(Jasminum.window_handles[0]) #切换窗口,
# 倒数为0的窗口 Jasminum.get_screenshot_as_file(str(time.time_ns()) + "注册错误信息.png")  ########错误截图,
# 格式.png前面加名字可以对进行错误的截图进行命名(不加则python默认命名) self.qudong.get_screenshot_as_file("./image/错误信息.png".format(
# time.strftime("%Y_%m_%d_%H_%M_%S")))


# send_keys(Keys.CONTROL,'a') #全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') #负责（Ctrl+C）
# send_keys(Keys.CONTROL,'v') #粘贴（Ctrl+V）
# send_keys(Keys.CONTROL,'x') #剪切（Ctrl+X）
# 回车  Keys.ENTER
# 删除  Keys.BACK_SPACE
# 空格  Keys.SPACE
# 制表符 Keys.TAB
# 回退 Keys.ESCAPE
# 刷新  Keys.F5
# 导入键盘操作模块
# from selenium.webdriver.common.keys import Keys
# driver.find_element_by_id('xx').send_keys(Keys.CONTROL, 'a')  # 全选操作
# driver.find_element_by_id("xx").send_keys(Keys.ENTER)  # 通过回车键来代替鼠标的左键


# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
#
# send_keys(Keys.SPACE) 空格键(Space)
#
# send_keys(Keys.TAB) 制表键(Tab)
#
# send_keys(Keys.ESCAPE) 回退键（Esc）
#
# send_keys(Keys.ENTER) 回车键（Enter）
#
# send_keys(Keys.CONTROL,’a’) 全选（Ctrl+A）
#
# send_keys(Keys.CONTROL,’c’) 复制（Ctrl+C）
#
# send_keys(Keys.CONTROL,’x’) 剪切（Ctrl+X）
#
# send_keys(Keys.CONTROL,’v’) 粘贴（Ctrl+V）


# context_click() 右击
# double_click() 双击
# drag_and_drop() 拖动
# move_to_element() 移动

# # name定位
# driver.find_element_by_name("操作控件元素的里name属性").clear()
# driver.find_element_by_name("操作控件元素的里name属性").send_keys("输入内容")
#
# # xpath定位Xpath在源代码也上右击需要操作的元素可以找到直接复制。
# driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div/input").send_keys("admin.syzg")
#
# # class_name定位
# driver.find_element_by_class_name("操作控件元素的里class-name属性").click()#点击操作
#
# # id定位
# driver.find_element_by_id("操作控件元素的里id属性").click()
#
# # link_text定位，通过文本定位
# driver.find_element_by_link_text(" 操作控件元素标签后的文本内容").click()
#
# # partial_link_text定位模糊搜索文本定位
# driver.find_element_by_partial_link_text("操作控件元素标签后一本分文本内容").click()
#
# # css_selector定位和xpath定位法的操纵相同。写法和css相同
# #元素的ID
# driver.find_element_by_css_selector("#res_title").send_keys("测试文档")
# #元素的类。
# driver.find_element_by_css_selector(".res_title").send_keys("测试文档")
