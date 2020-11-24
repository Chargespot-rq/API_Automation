#!coding = utf-8
import xlrd
def readExcel():
    data = list()
    book = xlrd.open_workbook("./mobile_login.xls")
    sheet = book.sheet_by_index(0)
    for item  in range(1,sheet.nrows):
        data.append(sheet.row_values(item))
    return data
#print(readExcel())