#!coding = utf-8
import yaml
import json
def readYaml():
    with open("./mobile_login.yaml","r",encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))


#print(readYaml()[0]["url"])
# print(readYaml())
#print(type(readYaml()))
'''
print(readYaml()["body"])
print(readYaml()["response"])
print(readYaml())

print(type((readYaml()["url"])))
print(type(readYaml()["body"]))
print(type(readYaml()["response"]))'''
# for item in readYaml():
#        print(item)