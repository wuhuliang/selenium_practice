# coding = utf-8

import xlrd

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

data = open_excel('F:\python practice\selenium_practice\\auto_testCase.xlsx')
table = data.sheet_by_name('login')
nrows = table.nrows #行数
colnames =







open_excel('hhhhhh')
