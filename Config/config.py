#配置py文档
from Commom.Logview import *
from Commom.Get_report import *

#测试环境请求头部验证
header_data = {"Terminal":"java","Authorization":"OPz2BJ6EJJV7stc2UxwRCPMG"}

#定义及生成日志路径
ilog = Logger('./Log/all.log', level='debug')
elog = Logger('./Log/error.log', level='error')

# 发送邮箱服务器
mail_smtp = 'smtp.sina.cn'
# 发送邮箱用户名/密码
mail_user = '17728193080@sina.cn'
mail_pwd = 'jxsg2018.'
# 发送邮箱
sendto = '17728193080@sina.cn'


#报告接收人
receivers = ['benvin1993@gmail.com','hongzhihong@dingtalk.com','xyunkai@dingtalk.com']

