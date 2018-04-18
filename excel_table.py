# coding=utf-8

import xlrd

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)

# 根据索引获取excel表格中的数据
# （参数1：文件路径）（参数2：列名所在的行的索引）（参数3：表的索引）
def excel_table_byindex(file,colname_index=0,table_index=0):
    # 打开文件
    data = open_excel(file)
    # 获取工作表
    table = data.sheet_by_index(table_index)
    # 获取行数
    nrows = table.nrows
    # 获取所有列名
    colnames = table.row_values(colname_index)
    # 定义一个空列表
    list = []

    # range()左闭右开，第0行是列名，从第1行开始
    for rownum in range(1, nrows):
        # 获取整行数据
        row = table.row_values(rownum)
        if row:
            # 定义字典存放用户名密码
            app = {}
            # 确定列的范围
            for i in range(len(colnames)):
                # i=0，获取key(username)
                # i=1，获取key(password)
                app[colnames[i]] = row[i]
            # 获取测试数据组存入列表
            list.append(app)

    return list

