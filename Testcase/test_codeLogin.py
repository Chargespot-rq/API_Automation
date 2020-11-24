#!coding = utf-8
#验证码登录
from Params.Open_json import readJson
from Commom.Requester import *
from Config.config import *
import pytest
import json
@pytest.mark.parametrize("data", readJson())
def test_json_login(data):
    """Json参数化"""
    r = method_post(header_data,data["request"]["url"],data["request"]['body'])
    #r = requests.post(headers=header_data,url=data["request"]["url"],data=data["request"]['body'])
    ilog.logger.info('json参数化login')
    ilog.logger.info('预期结果：%s'%data["response"])
    ilog.logger.info('实际结果：%s' %r.json()['dataInfo'])
    try:
        assert r.json()['dataInfo']==data["response"]
    except:
        elog.logger.error('数据不一致')
        assert False
    else:
        ilog.logger.info('测试通过！')