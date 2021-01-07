''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#作者：cacho_37967865
#博客：https://blog.csdn.net/sinat_37967865
#文件：pymysqlModel.py
#日期：2018-10-22
#备注：pip install pymysq  pymysql是Python中操作MySQL的模块   F:\python_env\PaChong_env
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import xlrd
import xlwt
from xlutils.copy import copy

sample_file = 'F:\pythonFile\\invoice GIL.xls'
invoice_name = 'GIL.xls'


# 发票模板：需要修改的地方（动态）
def invoice():
    data = xlrd.open_workbook(sample_file)
    table = data.sheets()[0]
    a = table.cell_value(7, 1)
    b = table.cell_value(8, 5)
    print(a, b)


# 获取发票需要的动态参数：第3行第2列发票号invoice，第3行第8列姓名name
def get_excel_data(packing_file):
    data = xlrd.open_workbook(packing_file)
    table = data.sheets()[0]
    nrows = table.nrows
    num = 0
    data = []
    for i in range(2, nrows):
        row = []
        invoice_no = table.cell_value(i, 1)
        name = table.cell_value(i, 7)
        if invoice_no != '':
            num = num + 1
            row.append(invoice_no)
            row.append(name)
            data.append(row)
    print('总发票数量：', num)
    return data


# TypeError: descriptor 'decode' requires a 'bytes' object but received a 'NoneType'
# F:\python_env\PaChong_env\lib\site-packages\\xlwt\UnicodeUtils.py
def make_excel(invoice_no, name):
    width = 256 * 8  # 8个字符宽
    # 字体和格式
    font = xlwt.Font()
    font.height = 240  # 12号字体
    font.bold = True
    font.name = 'Times New Roman'
    style = xlwt.XFStyle()
    style.font = font
    invoice = 'F:\pythonFile\\' + invoice_no + ' ' + invoice_name
    data = xlrd.open_workbook(sample_file, formatting_info=True)
    new_excel = copy(data)
    ws = new_excel.get_sheet(0)  # 获取第一个sheet
    first_col = ws.col(0)  # 第一列
    first_col.width = width  # 第一列宽
    ws.write(7, 1, name, style)  # B8(7,1)
    ws.write(8, 5, invoice_no, style)  # F9(8,5)
    new_excel.save(invoice)


def mk_invoices():
    packing_file = 'F:\pythonFile\\packing.xlsx'
    data = get_excel_data(packing_file)  # 获取所需参数
    for info in data:
        invoice_no = info[0]
        name = info[1]
        print(invoice_no, name)
        make_excel(invoice_no, name)


if __name__ == '__main__':
    mk_invoices()