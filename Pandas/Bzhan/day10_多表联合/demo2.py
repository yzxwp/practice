import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/016/Student_Score.xlsx", engine="openpyxl", sheet_name='Students',
                       index_col="ID")
    pf2 = pd.read_excel("../day09_图形的生产/demo/016/Student_Score.xlsx", engine="openpyxl", sheet_name='Scores',
                        index_col="ID")
    print(pf.head())
    print(pf2.head())
    # inner join
    table = pf.join(pf2)
    print(table)
    # left join
    table = pf.join(pf2, how='left')
    print(table)
    # right join,并将缺失的补充为0
    table = pf.join(pf2, how='right').fillna(0)
    print(table)


if __name__ == '__main__':
    way()
