#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: 484002966@qq.com

import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import yagmail


# 安装依赖库pip3 install zmail
# 安装依赖库pip3 install yagmail
# smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
class SendEmail:
    def __init__(self, smtp_addr, username, password, recv,
                 title, content=None, file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.smtp = None

    # 发送邮件方法
    def send_mail(self):
        # MIME
        msg = MIMEMultipart()
        # 初始化邮件信息
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.recv
        # 邮件附件
        # 判断是否附件
        if self.file:
            # MIMEText读取文件
            att = MIMEText(open(self.file).read())
            # 设置内容类型
            att["Content-Type"] = 'application/octet-stream'
            # 设置附件头
            att["Content-Disposition"] = 'attachment;filename="%s"' % self.file, 'utf-8'
            # 将内容附加到邮件主体中
            msg.attach(att)
        # 登录邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_addr, port=25)
        self.smtp.login(self.username, self.password)
        # 发送邮件
        self.smtp.sendmail(self.username, self.recv, msg.as_string())


if __name__ == "__main__":
    # i = 0
    # while i < 5:
    #     try:
    #         yag_server = yagmail.SMTP(user='484002966@qq.com', password='zyfuhyuglcqjbgij', host='smtp.qq.com')
    #         email_to = ['484002966@qq.com', '2807758094@qq.com']  # 接收的用户 #这里可以放多个用户的邮箱进行批量发送
    #         email_title = 'allure测试报告'  # 标题
    #         email_content = '<a href="https://www.baidu.com/">百度</a>'  # 内容
    #         email_attachments = [r'C:\Users\Administrator\a\Apis\测试报告.jpg']  # 附件内容 可以放多张和单张
    #         yag_server.send(email_to, email_title, email_content, email_attachments)  # send发送
    #         yag_server.close()
    #         time.sleep(2)
    #         i = i+1
    #         print("邮件成功发送了:", i)
    #     except:
    #         print("!!!!邮件发送失败!!!!")

    i = 1
    while i:
        try:
            yag_server = yagmail.SMTP(user='484002966@qq.com', password='zyfuhyuglcqjbgij', host='smtp.qq.com')
            email_to = ['484002966@qq.com', '2807758094@qq.com']  # 接收的用户 #这里可以放多个用户的邮箱进行批量发送
            email_title = 'allure测试报告'  # 标题
            email_content = '<a href="https://www.baidu.com/">百度</a>'  # 内容
            email_attachments = [r'C:\Users\Administrator\a\Apis\测试报告.jpg']  # 附件内容 可以放多张和单张
            yag_server.send(email_to, email_title, email_content, email_attachments)  # send发送
            yag_server.close()
            time.sleep(2)
            i = i + 1
            if i > 3:
                break
            print("邮件成功发送了:", i)
        except:
            print("!!!!邮件发送失败!!!!")
