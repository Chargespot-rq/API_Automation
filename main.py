#!coding = utf-8
import time
import pytest
from Commom.Send_mail import *

if __name__ == '__main__':
    pytest.main(
        ['--html=./Report/report%s.html' % time.strftime("_%Y-%m-%d %H%M%S"), '-s', '-vv',
         "--self-contained-html",'Testcase/test_codeLogin.py'])
#
# 发送邮箱报告
# send_email()
