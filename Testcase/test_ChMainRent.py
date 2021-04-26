# -*- coding: utf-8 -*-
from Config.config import *
from Commom.Requester import *
import requests
import pytest

'''大陆租借主流程'''


class Test_Ch_main_rent_wechat():

    # 登录
    def test_login(self):
        url = test_evrmt + '/v4/member/sign/applets'
        data = {'code': '', 'openId': '', 'country': '', 'province': '', 'city': '', 'languageCode': ''}
        login_re = method_post(header_data, url, data)

    # 租借
    def test_rent(self):
        # 获取用户id
        uid = self.login_re[id]
        # 创建免押授权
        url_order_create = test_evrmt + '/v1/wechat/create/rent/bill'
        data_order_create = {'memberId': uid, 'terminalId': ''}
        re_order_create = method_post(header_data, url_order_create, data_order_create)
        # 授权下单
        url_wechat_rent = test_evrmt + '/v1/wechat/create/rent/bill'
        data_wechat_rent = {'memberId': 'uid', 'terminalId': 'type', 'orderId': '', 'formId': '', 'openId': '',
                            'isLowPower': ''}
        re_wechat_rent = method_post(header_data, url_wechat_rent, data_wechat_rent)

    # 归还结算
    def test_close_order(self):
        pass

    # 退款
    def test_return_rate(self):
        pass

    # 充值
    def test_charge(self):
        pass
