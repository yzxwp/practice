import pandas as pd


def way():
    pf = pd.read_excel('./1.xlsx', engine='openpyxl', index_col='id')
    # 按照价格从低到高
    pf.sort_values(by='price', inplace=True)
    # 按照价格从高到低
    pf.sort_values(by='price', inplace=True, ascending=False)
    # 按照多个选项排序
    pf.sort_values(by=["worth", 'price'], inplace=True)
    # 按照多个选项排序,并且对某一列排序
    pf.sort_values(by=["worth", 'price'], inplace=True, ascending=[True, False])
    print(pf)


if __name__ == '__main__':
    way()
