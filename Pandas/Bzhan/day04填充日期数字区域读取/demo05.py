import pandas as pd
from datetime import date, timedelta


def add_mouth(data, md):
    yd = md // 12
    m = data.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(data.year + yd, m, data.day)


def way():
    # skiprows=5 跳过头上的5个空格
    # usecols="F:I" 展示那些数据
    # dtype={"id": str}类型
    pf = pd.read_excel("./1.xlsx", engine="openpyxl", skiprows=5, usecols="F:I", index_col=None,
                       dtype={"id": str, "enable": str, "date": str})
    # print(pf)
    # print(pf['id'])
    # print(pf['id'])
    # print(type(pf['id']))
    pf['id'].at[0] = 1000
    # print(pf['id'])
    data = date(2018, 1, 1)
    for i in pf.index:
        pf['id'].at[i] = i + 1
        pf['enable'].at[i] = "yes" if i % 2 == 0 else "NO"
        # 加天
        # pf['date'].at[i] = data + timedelta(days=i)
        # 加年
        # pf['date'].at[i] = date(data.year + i, data.month, data.day)
        pf['date'].at[i] = add_mouth(data, i)
    print(pf)


if __name__ == '__main__':
    way()
