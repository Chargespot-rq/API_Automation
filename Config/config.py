#配置py文档
from Commom.Logview import *

#测试环境请求头部验证
header_data = {"Terminal":"java","Authorization":"OPz2BJ6EJJV7stc2UxwRCPMG"}

#定义及生成日志路径
ilog = Logger('./Log/all.log', level='debug')
elog = Logger('./Log/error.log', level='error')