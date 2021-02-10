import pandas as pd


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/019/Students.xlsx", engine="openpyxl", index_col="ID")
    print(pf)
    temp = pf[["Test_1", 'Test_2', 'Test_3']]
    print(temp)
    raw_sum = temp.sum(axis=1)
    raw_mean = temp.mean(axis=1)
    print(raw_sum)
    print(raw_mean)
    pf["Totle"] = raw_sum
    pf["Average"] = raw_mean
    print(pf)
    col_mean = pf[["Test_1", 'Test_2', 'Test_3', "Totle", "Average"]].mean()
    col_mean["Name"] = "Summary"
    pf = pf.append(col_mean, ignore_index=True)
    print(pf)


if __name__ == '__main__':
    way()
