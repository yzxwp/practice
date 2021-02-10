import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/016/Student_Score.xlsx", engine="openpyxl", sheet_name='Students')
    pf2 = pd.read_excel("../day09_图形的生产/demo/016/Student_Score.xlsx", engine="openpyxl", sheet_name='Scores')
    print(pf.head())
    print(pf2.head())
    # inner join
    table = pf.merge(pf2, on='ID')
    print(table)
    # left join
    table = pf.merge(pf2, how='left', on='ID')
    print(table)
    # right join,并将缺失的补充为0
    table = pf.merge(pf2, how='right', on='ID').fillna(0)
    print(table)


if __name__ == '__main__':
    way()
