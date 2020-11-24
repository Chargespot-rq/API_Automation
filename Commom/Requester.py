#!coding = utf-8
import requests
def method_post(header,url,data):
    res = requests.post(headers=header,url=url,data=data)
    return res

def method_get(header,url,data=None):
    res = requests.get(headers=header,url=url,data=data)
    return res
