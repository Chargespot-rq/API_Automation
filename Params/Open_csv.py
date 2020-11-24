#!coding = utf-8
import csv
def readCsv():
    data = list()
    with open("./mobile_login.csv","r") as f:
        reader = csv.reader(f)
        #忽略表头
        next(reader)
        for item in reader:
            data.append(item)
    return data


# for item in readCsv():
#     print(item)