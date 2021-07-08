#!/usr/bin/env python
# coding=utf-8

'''
python发送email测试
源码地址:
https://juejin.cn/post/6981334508553371655
'''

# SMTP服务器,这里使用qq邮箱,其他邮箱自行百度
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_HOST = 'smtp.qq.com'
# 发送邮件的代理邮箱
EMAIL_HOST_USER = 'xxxxxx@xxx.com'
# 在邮箱中设置的客户端授权密码, 注意这里不是邮箱密码,关于如何获取邮箱授权码,请自行百度~~~
EMAIL_HOST_PASSWORD = 'xxxxxxx'


class SendEmailManager(object):

    def __init__(self, **kwargs):
        # 初始化参数
        self.email_host = EMAIL_HOST
        self.email_host_user = EMAIL_HOST_USER
        self.email_host_pass = EMAIL_HOST_PASSWORD
        self.kwargs = kwargs

    def _get_conf(self, key):
        # 获取配置参数
        value = self.kwargs.get(key)
        if key != "attach_file_list" and (value is None or value == ''):
            raise Exception("configuration parameter '%s' cannot be empty" % key)
        return value

    def _init_conf(self):
        # 初始化配置参数
        print(self._get_conf('receives'))
        self.receives = self._get_conf('receives')
        self.msg_subject = self._get_conf('msg_subject')
        self.msg_content = self._get_conf('msg_content')
        self.msg_from = self._get_conf('msg_from')
        # attachment
        self.attach_file_list = self._get_conf('attach_file_list')

    def _login_email(self):
        # 登录邮箱服务器
        try:
            server = smtplib.SMTP_SSL(self.email_host, port=465)
            # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
            server.set_debuglevel(1)
            # 登录邮箱
            server.login(self.email_host_user, self.email_host_pass)
            return server
        except Exception as e:
            print("mail login exception:", e)
            raise e

    def _make_mail_msg(self):
        # 构建邮件对象
        msg = MIMEMultipart()
        msg.attach(MIMEText(self.msg_content, 'plain', 'utf-8'))
        # 邮件主题
        msg['Subject'] = Header(self.msg_subject, "utf-8")
        # 发件人邮箱信息
        msg['From'] = "<%s>" % self.msg_from
        # msg['From'] = Header(self.msg_from + "<%s>" % self.email_host_user, "utf-8")
        msg['To'] = ",".join(self.receives)
        print("---", self.attach_file_list)
        if self.attach_file_list:
            for i, att in enumerate(self.attach_file_list):
                # 构造附件，传送当前目录下的文件
                if not att:
                    break
                att_i = MIMEText(open(att, 'rb').read(), 'base64', 'utf-8')
                att_i["Content-Type"] = 'application/octet-stream'
                # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
                att_i["Content-Disposition"] = 'attachment; filename="%s"' % att
                msg.attach(att_i)
        return msg

    def do_send_mail(self):
        # 邮件发送
        try:
            self._init_conf()
            server = self._login_email()
            msg = self._make_mail_msg()
            server.sendmail(self.email_host_user, self.receives, msg.as_string())
            server.close()
            print("发送成功！")
        except Exception as e:
            print("邮件发送异常", e)


if __name__ == "__main__":
    mail_conf = {
        'msg_from': 'xxxxx@xxxx.com',  # 邮件发送者的地址
        'receives': ['xxxxx@xxxx.com',],  # 邮件接收者的地址,这是个list，因为邮件的接收者可能不止一个
        'msg_subject': 'Python发送邮件测试',  # 邮件的主题
        'msg_content': 'hello',  # 邮件的内容
        'attach_file_list': {"test.py": "test.py", "test.txt": "./test.txt"},  # 为附件文件路径列表，也可没有这项
    }

    manager = SendEmailManager(**mail_conf)
    manager.do_send_mail()

