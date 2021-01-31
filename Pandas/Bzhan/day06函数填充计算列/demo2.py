import pandas as pd
from datetime import date, timedelta


def add_mouth(data, md):
    yd = md // 12
    m = data.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(data.year + yd, m, data.day)


def add_2(x):
    return x + 2


def way():
    # skiprows=5 跳过头上的5个空格
    # usecols="F:I" 展示那些数据
    # dtype={"id": str}类型
    pf = pd.read_excel("./44.xlsx", engine="openpyxl", index_col='id')
    # pf['price'] = pf['list'] * pf['discount']
    # pf['price'] = pf['list'] * 0.8
    # for i in pf.index:
    #     pf['price'] = pf['list'].at[i] * pf['discount'].at[i]
    # for i in range(2, 5):
    #     pf['price'] = pf['list'].at[i] * pf['discount'].at[i]
    # for i in pf.index:
    #     pf['list'] = pf['list'].at[i] + 2
    # pf['list'] = pf['list'].apply(add_2)
    pf['list'] = pf['list'].apply(lambda x: x + 2)
    print(pf)


if __name__ == '__main__':
    way()
