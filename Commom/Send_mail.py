#!coding = utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Commom.Get_report import *
from Config.config import *
import smtplib
# 发送邮件，发送最新测试报告html
def send_email():
    # 打开文件
    f = open(new_file(), 'r',encoding='utf-8')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    # print u'打印'
    #print (mail_body)
    # 关闭文件
    f.close()

    # 发送邮箱服务器
    smtpserver = mail_smtp
    # 发送邮箱用户名/密码
    user = mail_user
    password = mail_pwd
    # 发送邮箱
    sender = sendto

    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
    #receiver = ['liuwb@shushangyun.com', '13798963487@139.com']
    receiver = receivers

    # 发送邮件主题
    subject = 'API自动化测试报告'
    msg = MIMEMultipart('mixed')
    # 发送html附件
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    # 重新命名附件
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="test_Report.html"'
    msg.attach(msg_html)

    # 以普通附件的方式发送会出错
    # msg_html = MIMEText(mail_body,'base64','utf-8')
    # msg_html["Content-Type"] = 'application/octet-stream'
    # msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
    # msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = 'testgroup<17728193080@sina.cn>'

    # 单个收件人
    # msg['To'] = receiver
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    # 下句报错更改下服务器端口25/587/465或未开起授权码
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()