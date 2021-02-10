import pandas as pd


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/021/Videos.xlsx", engine="openpyxl",
                       index_col='Month')
    print(pf)
    pf2 = pf.transpose()
    print(pf2)


if __name__ == '__main__':
    way()
