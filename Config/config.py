# 配置py文档
from Commom.Logview import *
from Commom.Get_report import *
from Commom.MysqlHelper import *

# 测试环境请求头部验证
header_data = {"Terminal": "java", "Authorization": "OPz2BJ6EJJV7stc2UxwRCPMG"}

# 定义及生成日志路径
ilog = Logger('./Log/all.log', level='debug')
elog = Logger('./Log/error.log', level='error')

# 发送邮箱服务器
mail_smtp = 'smtp.sina.cn'
# 发送邮箱用户名/密码
mail_user = '17728193080@sina.cn'
mail_pwd = 'jxsg2018.'
# 发送邮箱
sendto = '17728193080@sina.cn'

# 报告接收人
receivers = ['benvin@dingtalk.com', 'hongzhihong@dingtalk.com', 'xyunkai@dingtalk.com']

# 数据库配置
mysql = MysqlHelper(host='47.52.4.209', port=5666, db='cdb', user='cdb', passwd='cdbChargespot@2020',
                    charset='utf8')
# re = mysql.all("select id,store_value from member WHERE mobile = '13798963487'")
# print(type(re))
