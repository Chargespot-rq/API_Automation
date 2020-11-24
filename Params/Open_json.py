#!coding = utf-8
import json
def readJson():
  return  json.load(open('./Params/mobile_login.json','r'))['item']
#print(readJson())