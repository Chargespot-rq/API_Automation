#!coding = utf-8
import time
import pytest
from Commom.Send_mail import *
def run():
    if __name__ == '__main__':
         pytest.main(['--html=./Report/report%s.html'%time.strftime("_%Y-%m-%d %H%M%S"),'-s','-v',"--self-contained-html"])

    #发送邮箱报告
    send_email()
run()