import pandas as pd


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/020/Students_Duplicates.xlsx", engine="openpyxl",
                       index_col="ID")
    print(pf)
    pf.drop_duplicates(subset="Name", inplace=True, keep="first")
    print(pf)
    pf = pd.read_excel("../day09_图形的生产/demo/020/Students_Duplicates.xlsx", engine="openpyxl",
                       index_col="ID")
    pf.drop_duplicates(subset="Name", inplace=True, keep="last")
    print(pf)
    # 查处重复数据
    pf = pd.read_excel("../day09_图形的生产/demo/020/Students_Duplicates.xlsx", engine="openpyxl")
    dupe = pf.duplicated(subset="Name")
    print(dupe)
    print(dupe.any())
    # 找到重复数量
    dupe = dupe[dupe == True]
    print(dupe)
    print(dupe.index)
    print(pf.iloc[dupe.index])


if __name__ == '__main__':
    way()
